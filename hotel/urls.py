from django.urls import path
from .views import TravelView, KlasView, HotelView

urlpatterns = [
    path('', TravelView.as_view()),
    path('<int:pk>', TravelView.as_view()),
    path('klass', KlasView.as_view()),
    path('klass/<int:pk>', KlasView.as_view()),
    path('hotel', HotelView.as_view()),
    path('hotel/<int:pk>', HotelView.as_view())
]