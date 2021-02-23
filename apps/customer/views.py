from django.http import request
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .models import ProfilePage
from django.contrib.auth import get_user_model


User = get_user_model()


class ProfilePageView(LoginRequiredMixin, TemplateView):
    template_name = 'profile/profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['user'] = self.request.user.profilepage
        return context


def user_profile_update(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        user = User.objects.get(username=request.user.username)
        user.username = name
        user.email = email
        profile = ProfilePage.objects.get(user__username = request.user.username)
        profile.phone = phone
        user.save()
        profile.save()
        success_message = 'User was updated successfully, Please resfresh the page to see updates'
        return HttpResponse(success_message)
