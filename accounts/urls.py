from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('user/',views.userProfile, name="user-page"),
    path('account',views.accountSettings, name="account"),
    path('customer/<str:pk>', views.customer, name="customer"),
    path('create_order/<str:pk>', views.createOrder, name="create_order"),
    path('update_order/<str:pk>', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>', views.deleteOrder, name="delete_order"),

    path('signup/',views.signupuser, name = 'signupuser'),
    path('login/',views.loginuser, name ="loginuser"),
    path('logout/',views.logoutuser, name = 'logoutuser'),

    path('password_reset/',
        auth_views.PasswordResetView.as_view(template_name = 'accounts/password_reset.html'), 
        name = "password_reset"
    ),
    path('password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name = 'accounts/password_reset_sent.html'), 
        name = "password_reset_done"
    ),
    path('password_reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name = 'accounts/password_reset_form.html'), 
        name = "password_reset_confirm"
    ),
    path('password_reset/complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name = 'accounts/password_reset_done.html'), 
        name = "password_reset_complete"
    ),
    path('password_change',
        auth_views.PasswordChangeView.as_view(template_name = 'accounts/password_change.html'), 
        name = "password_change"
    ),

    path('password_change/done',
        auth_views.PasswordChangeDoneView.as_view(template_name = 'accounts/password_change_done.html'), 
        name = "password_change_done"
    ),
]