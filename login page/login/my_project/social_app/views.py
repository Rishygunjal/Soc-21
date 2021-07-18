from django.shortcuts import render

# Create your views here.
from allauth.socialaccount.adaptor import DefaultSocialAccountAdapter
from django.shortcuts import render
from allauth.account.adapter import DefaultAccountAdapter
from allauth.exceptions import ImmediateHttpResponse
from django.shortcuts import render_to_response

class MySocialAccount(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        u = sociallogin.account.user
        if not u.email.split('@')[1] == "example.com":
            raise ImmediateHttpResponse(render_to_response('error.html'))