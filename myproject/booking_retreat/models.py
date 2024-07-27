from django.db import models
from sqlalchemy import String ,create_engine ,Column ,Integer ,ForeignKey ,ARRAY ,Date
from sqlalchemy.orm import  Mapped ,mapped_column, declarative_base ,sessionmaker ,relationship
from django.forms import model_to_dict
from sqlalchemy.engine import URL
from sqlalchemy.sql import func
from sqlalchemy.types import TypeDecorator
import datetime
from dotenv import load_dotenv
import os

load_dotenv()

url = URL.create(
    drivername=os.environ.get('DRIVERNAME'),
    username=os.environ.get('USERNAME_PROD'),
    password=os.environ.get('PASSWORD'),
    host=os.environ.get('HOST'),
    database=os.environ.get('DATABASE'),
    query={
        'sslmode': 'require'
    }
)

postgresql_engine = create_engine(
    url, 
    echo=False
)

connection = postgresql_engine.connect()
Session = sessionmaker(bind=postgresql_engine)
session = Session()
Base = declarative_base()


class TimestampDate(TypeDecorator):
    impl = Integer

    def process_bind_param(self, value, dialect):
        if isinstance(value, datetime.date):
            return int(value.timestamp())
        return value

    def process_result_value(self, value, dialect):
        if value:
            return datetime.datetime.fromtimestamp(value).date()
        return None
    
class Retreat(Base):
    __tablename__ ='retreat'

    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String(150))
    location = mapped_column(String(150))
    price = mapped_column(String(150))
    description = mapped_column(String(1000))
    date = mapped_column(TimestampDate)
    type = mapped_column(String(150))
    condition = mapped_column(String(150))
    image = mapped_column(String(150))
    tag = mapped_column(ARRAY(String)) 
    duration = mapped_column(Integer)

    retreats = relationship("Booking" ,back_populates="retreat")
    
    def to_dict(self):
        return {
            "id": self.id,
            "title" : self.title,
            "location": self.location,
            "price": self.price,
            "description": self.description,
            "date": self.date,
            "type": self.type,
            "condition": self.condition,
            "image": self.image,
            "tag": self.tag,
            "duration": self.duration
        }
    
    

class Booking(Base):
    __tablename__ = 'booking'
    
    id =  mapped_column( Integer,primary_key=True)
    user_id = mapped_column(Integer)
    user_name = mapped_column(String(150))
    user_email = mapped_column(String(150))
    user_phone = mapped_column(String(150))
    retreat_id = mapped_column(Integer, ForeignKey('retreat.id'))
    retreat_title = mapped_column(String(150))
    retreat_location = mapped_column(String(150))
    retreat_price = mapped_column(String(150))
    retreat_duration = mapped_column(Integer)
    payment_details = mapped_column(String(150))
    booking_date = mapped_column(Date)
    
    retreat = relationship("Retreat", back_populates="retreats")
    
    def to_dict(self):
        return {
            "id": self.id,
            "user_id" : self.user_id,
            "user_name": self.user_name,
            "user_email": self.user_email,
            "user_phone": self.user_phone,
            "retreat_id": self.retreat_id,
            "retreat_title": self.retreat_title,
            "retreat_location": self.retreat_location,
            "retreat_price": self.retreat_price,
            "retreat_duration": self.retreat_duration,
            "payment_details": self.payment_details,
            "booking_date": self.booking_date
        }


Base.metadata.create_all(postgresql_engine)
    