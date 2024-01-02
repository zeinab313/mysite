
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
# from django.contrib.auth import  get_user_model
from django.contrib.auth.views import (PasswordChangeView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)

from django.urls import reverse_lazy
from .forms import *

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            userinput = request.POST['username']
            try:
                username = User.objects.get(email=userinput).username
            except User.DoesNotExist:
                username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.add_message(request,messages.SUCCESS,'Login was successful')
                return redirect('/')
            else:
                 messages.add_message(request,messages.ERROR,'The desired person was not found')
        return render(request, "accounts/login.html")
    else:
          return redirect('/')

@login_required
def logout_view(request):
    #  if request.user.is_authenticated:
          logout(request)
          return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
              form=SignUpForm(request.POST)
              if form.is_valid():
                form.save()
                return redirect('/')
        # form=UserCreationForm()
        form=SignUpForm()
        context={'form':form}
        return render(request,'accounts/signup.html',context)
    else:
          return redirect('/')



# Customized password change and reset views

# class ChangePasswordView(PasswordChangeView):
#     template_name = 'accounts/change_password.html'
#     success_url = reverse_lazy('account:user-setting')
#     form_class = ChangePasswordForm

class PasswordReset(PasswordResetView):
    template_name="accounts/password_reset_form.html"
    success_url=reverse_lazy("accounts:password_reset_done")

class PasswordResetDone(PasswordResetDoneView):
    template_name="accounts/password_reset_done.html"
    success_url=reverse_lazy("accounts:password_reset_confirm")

class PasswordResetConfirm(PasswordResetConfirmView):
    template_name="accounts/password_reset_confirm.html"
    success_url=reverse_lazy("accounts:password_reset_complete")

class PasswordResetComplete(PasswordResetCompleteView):
    template_name="accounts/password_reset_complete.html"

