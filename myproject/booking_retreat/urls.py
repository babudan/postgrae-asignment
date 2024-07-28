from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import Bookingview ,RetreatView



urlpatterns = [
    # path('test/', csrf_exempt(Testview.as_view()), name='testview'), 
    path('bookings/', csrf_exempt(Bookingview.as_view()), name='bookingview'),
    path('retreat/', csrf_exempt(RetreatView.as_view()), name='retreatview'),   
]  