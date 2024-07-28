from booking_retreat.models import Retreat
from sqlalchemy import or_, and_

def build_search_condition(search):
    search_condition_filter = []
    valid_date = False
    valid_duration = False
    
    try:
        search_int = int(search)
        search_condition_filter.append(Retreat.date == search_int)
        valid_date = True
    except ValueError:
        pass
    if not valid_date:
        try:
            search_int_duration = int(search)
            search_condition_filter.append(Retreat.duration == search_int_duration)
            valid_duration = True
        except ValueError:
            pass

    # Always add string search conditions
    search_condition_filter.extend([
                    Retreat.title.ilike(f"%{search}%"),
                    Retreat.location.ilike(f"%{search}%"),
                    Retreat.description.ilike(f"%{search}%"),
                    Retreat.price.ilike(f"%{search}%"),
                    Retreat.type.ilike(f"%{search}%"),
                    Retreat.condition.ilike(f"%{search}%"),
                    Retreat.tag.any(search),
    ])

    return or_(*search_condition_filter) if search_condition_filter else None