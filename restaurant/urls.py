from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('menu-items', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    
    path('booking', views.BookingView.as_view()),
    path('booking/<int:pk>', views.BookingSingleView.as_view()),
]
