from django.urls import path
from . import views

app_name="accounts"

urlpatterns = [
    #login
    path('login',views.login_view,name='login'),
    #logout
    path('logout',views.logout_view,name='logout'),
    #registrations/signup
    path('signup',views.signup_view,name='signup'),
    #forget password
    # path('password_reset',views.password_reset,name='password_reset'),
    # path('password_reset_done',views.password_reset_done,name='password_reset_done'),
    # path('password_reset_email',views.password_reset_email,name='password_reset_email'),
    # path('password_reset_confirm',views.password_reset_confirm,name='password_reset_confirm'),
    # path('password_reset_complete',views.password_reset_complete,name='password_reset_complete'),
#راه دوم
    # path('change/password',views.ChangePasswordView.as_view(),name="change-password"),
    path('password_reset', views.PasswordReset.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),



]
