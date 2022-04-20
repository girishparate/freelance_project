from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    # home dashboard
    path('', login_required(Dashboard.as_view()), name='home-dashboard'),

    # signup for members
    path('member-signup', SignupMember.as_view(), name='member-signup'),

    # login api for member
    path('member-login', SignupMember.as_view(), name='member-login'),

    # forgot password for member
    path('forgot-password/<email>', ForgotPasswordMember.as_view(), name='forgot-password')

]
