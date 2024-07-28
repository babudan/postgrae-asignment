from django.views.generic import View
from booking_retreat.responses import *
from booking_retreat.models import Session ,Booking ,Retreat
from booking_retreat.validation import Validation ,ValidationException
from sqlalchemy.exc import SQLAlchemyError
import json
from sqlalchemy import or_, and_
from booking_retreat.utils import build_search_condition
from django.db.models import Q
from myproject.settings.base import DATA_UPLOAD_MAX_MEMORY_SIZE


# class Testview(View):
#     def __init__(self):
#         self.response = {}
        
#     def get(self, request, *args, **kwargs):
#         return JsonResponse({'message': 'This is a test route!'})

class RetreatView(View):
    def __init__(self):
        self.response = {}

    def get(self, request, *args, **kwargs):
        session = Session()
        title = request.GET.get("title")
        location = request.GET.get("location")
        price = request.GET.get("price")
        description = request.GET.get("description")
        date = request.GET.get("date")
        type = request.GET.get("type")
        condition = request.GET.get("condition")
        image = request.GET.get("image")
        tag = request.GET.get("tag")
        duration = request.GET.get("duration")
        search = request.GET.get("search")
        page = int(request.GET.get("page", 1)) 
        limit = int(request.GET.get("limit", 10))
        
        try:
            q_objects = []
            if title:
                q_objects.append(Retreat.title == title)
            if location:
                q_objects.append(Retreat.location == location)  
            if price:
                q_objects.append(Retreat.price == price)
            if description:
                q_objects.append(Retreat.description == description)          
            if duration:
                duration_int = int(duration)
                q_objects.append(Retreat.duration == duration_int) 
            if date:
                date_int = int(date)
                q_objects.append(Retreat.date == date_int)    
            if type:
                q_objects.append(Retreat.type == type)
            if condition:
                q_objects.append(Retreat.condition == condition)
            if image:
                q_objects.append(Retreat.image == image)
            if tag:
                q_objects.append(Retreat.tag.any(tag))    
                
            if search:
                search_condition_filter = build_search_condition(search)
        
                q_objects.append(search_condition_filter)    
            
            pagination = (page -1) * limit    
            all_conditions = and_(*q_objects)  if q_objects else True 
            retreat_fetches = session.query(Retreat).filter(all_conditions).offset(pagination).limit(limit).all()
            
            result = [retreat_fetch.to_dict() for retreat_fetch in retreat_fetches]
            return JsonResponse({"success": False, 'data': result}, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def create_retreats(self, data_list):
        session = Session()
        chunk_size = 1000  # Process 1000 records at a time
        responses = []
        for i in range(0, len(data_list), chunk_size):
            chunk = data_list[i:i + chunk_size]  # Get the current chunk
            objs = []
            for data in chunk:
                title = data.get("title")
                location = data.get("location")
                price = data.get("price")
                description = data.get("description")
                date = data.get("date")
                type = data.get("type")
                condition = data.get("condition")
                image = data.get("image")
                tag = data.get("tag")
                duration = data.get("duration")
                
                try:
                    # Validation.validate_status(officialname, "officialname")
                    # Validation.validate_status(country, "country")

                    obj = Retreat(
                        title=title,
                        location=location,
                        price=price,
                        description=description,
                        date=date,
                        type=type,
                        condition=condition,
                        image=image,
                        tag=tag,
                        duration=duration,
                    )
                    objs.append(obj)
                except ValidationException as e:
                    responses.append({"res_str": f"Validation Error: {str(e)}", "status": 400})
                except Exception as e:
                    responses.append({"res_str": str(e), "status": 400})

            # Bulk create objects for the current chunk
            if objs:
                session.bulk_save_objects(objs)
                session.commit()
                responses.append({"res_str": f"{len(objs)} Retreat added successfully", "status": 200})

        return responses

    def post(self, request):
        content_length = request.META.get('CONTENT_LENGTH')
        if content_length and int(content_length) > DATA_UPLOAD_MAX_MEMORY_SIZE:
            return JsonResponse({"res_str": "Request body exceeded the maximum allowed size."}, status=400)

        data = json.loads(request.body.decode('utf-8'))
        if not isinstance(data, list):
            data = [data]

        try:
            responses = self.create_retreats(data)
            return JsonResponse(responses, safe=False, status=200)

        except ValidationException as e:
            return JsonResponse({"res_str": f"Validation Error: {str(e)}"}, status=400)
        except Exception as e:
            return JsonResponse({"res_str": str(e)}, status=400)
        
        
class Bookingview(View):
    def __init__(self):
        self.response = {}
    
    def create_booking(self ,data):
        session = Session()
        try:
            user_id = data.get("user_id")
            user_name = data.get("user_name")
            user_email = data.get("user_email")
            user_phone = data.get("user_phone")
            retreat_id = data.get("retreat_id")
            retreat_title = data.get("retreat_title")
            retreat_location = data.get("retreat_location")
            retreat_price = data.get("retreat_price")
            retreat_duration = data.get("retreat_duration")
            payment_details = data.get("payment_details")
            booking_date = data.get("booking_date")
            
            try:
                Validation.validate_field(user_id ,"user_id")
                Validation.validate_field(user_name ,"user_name")
                Validation.validate_field(user_email ,"user_email")
                Validation.validate_field(user_phone ,"user_phone")
                Validation.validate_field(retreat_id ,"retreat_id")
                Validation.validate_field(retreat_title ,"retreat_title")
                Validation.validate_field(retreat_location ,"retreat_location")
                Validation.validate_field(retreat_price ,"retreat_price")
                Validation.validate_field(retreat_duration ,"retreat_duration")
                Validation.validate_field(payment_details ,"payment_details")
                Validation.validate_field(booking_date ,"booking_date")

            except Exception as e:
                raise Exception(f"Validation Error: {str(e)}")
                
            retreat = session.query(Booking).filter_by(retreat_id=int(retreat_id) ,user_id=int(user_id)).first()
            if retreat:
                pass
                raise Exception("User already booked this retreat.")
            else:
                booking = Booking(
                user_id=user_id,
                user_name = user_name,
                user_email=user_email,
                user_phone=user_phone,
                retreat_id=retreat_id,
                retreat_title=retreat_title,
                retreat_location=retreat_location,
                retreat_price=retreat_price,
                retreat_duration=retreat_duration,
                payment_details=payment_details,
                booking_date=booking_date
                )
                session.add(booking)
                session.commit()
                return booking.to_dict()
        except SQLAlchemyError as e:
            session.rollback()
            return JsonResponse({'error': str(e)}, status=500)
        finally:
            session.close()    
    
    def post(self, request):
        user = request.user
        data = json.loads(request.body.decode('utf-8'))
        try:
            create_booking = self.create_booking(data)
            self.response["res_data"] = create_booking
        except Exception as e:
            self.response["res_str"] = str(e)
            # self.response["tech_err"] = str(e)
            return send_400(self.response)

        return send_200(self.response)        
        
        
        