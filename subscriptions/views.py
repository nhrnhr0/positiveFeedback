from django.shortcuts import render
from django.utils import timezone

from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from subscriptions.models import Subscription, SubPlant
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib import messages



@receiver(user_signed_up)
def user_signed_up_callback(sender, **kwargs):
    trailSubPlnat = SubPlant.objects.get(name='Trail')
    userSub = Subscription.objects.create(plant=trailSubPlnat, user=kwargs['user'], isActive=True, isCanceled=True, start_time=timezone.now(), end_time=timezone.now() + timezone.timedelta(days=14))

    print("user_signed_up!", userSub)

# Create your views here.
from .models import Subscription, SubPlant
def change_user_plan(request, *args, **kwargs):
    if request.method == "POST":
        planId = request.POST['submit']

        
        activeSubscriptions = Subscription.objects.filter(user=request.user, isActive=True)
        if activeSubscriptions:
            active = activeSubscriptions.first()
            timeoffset = active.end_time - timezone.now()
            activeSubscriptions.update(isActive=False, isCanceled=True)
        else:
            timeoffset = 0

        userSub = Subscription.objects.create(plant=SubPlant.objects.get(pk=planId), user=request.user, isActive=True, isCanceled=False, start_time=timezone.now(), end_time=timezone.now() + timezone.timedelta(days=30) + timeoffset)
        messages.add_message(request, messages.SUCCESS, 'account has been charged')
        return redirect('/accounts/profile')