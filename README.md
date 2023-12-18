Admin panel username: shivam
Admin panel password: super@pass

For registering new user  => http://127.0.0.1:8000/auth/users/
Listing menu items => http://127.0.0.1:8000/restaurant/menu-items
List of Bookings => http://127.0.0.1:8000/restaurant/booking


====================================Project-level URL routes=====================================
urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]


=======================================App-level URL routes=======================================
urlpatterns = [
    path('', views.index, name="index"),
    path('menu-items', views.MenuItemView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    
    path('booking', views.BookingView.as_view(), name='booking'),
    path('booking/<int:pk>', views.BookingSingleView.as_view()),
    
    path('api-token-auth', obtain_auth_token),
]
