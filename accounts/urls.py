from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk>', views.customer, name="customer"),
    path('create_order/<str:pk>', views.createOrder, name="create_order"),
    path('update_order/<str:pk>', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>', views.deleteOrder, name="delete_order"),

    path('signup/',views.signupuser, name = 'signupuser'),
    path('login/',views.loginuser, name ="loginuser"),
    path('logout/',views.logoutuser, name = 'logoutuser'),
]