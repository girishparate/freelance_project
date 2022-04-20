from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

# Create your views here.


""" This Api is work for loging into the system for member (company / organization). """
class LoginMember(View):
    def get(self, request):
        data = {
            'title' : 'Login for members'
        }
        return render(request, "member_login.html", data)

    def post(self, request):
        return HttpResponseRedirect('/')


""" This API will we used for signup and adding other personal information of member. """
class SignupMember(View):
    def get(self, request):
        data = {
            'title' : 'Signup for members'
        }
        return render(request, "member_signup.html", data)

    def post(self, request):
        return HttpResponseRedirect('/')


""" This API is to generate link for password reset"""
class LinkGeneration(View):
    def post(self, request):
        return HttpResponseRedirect('/')


""" This API is used for fogot password"""
class ForgotPasswordMember(View):
    def get(self, request, email):
        data = {
            'title' : 'Forgot password'
        }
        return render(request, "member_forgot_password.html", data)

    def post(self, request, email):
        return HttpResponseRedirect('/')


""" Dashboard """
class Dashboard(View):
    def get(self, request):
        data = {
            'title' : 'Dashboard'
        }
        return render(request, "dashboard.html", data)


