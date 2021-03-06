from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from core.models import Campain, Proof
from django.urls import reverse

from paypal.standard.forms import PayPalPaymentsForm



# Create your views here.
def generateReview(reuqest, id):
    print(id)
    campain = Campain.objects.get(pk=id)

    return render(request=reuqest, content_type="application/javascript",template_name='reviews.loader.js',   context={"campain":campain})
    #return HttpResponse("console.log('hey');", 

def testIndexView(request):
    return render(request, 'index.html' , {})

from .forms import CampainForm, ProfForm
def profileView(request, reviewToEdit=-1):
    if request.user.is_anonymous:
        return redirect('/accounts/login')


    campains = Campain.objects.filter(owner=request.user)
    proofs = Proof.objects.filter(owner=request.user)
    profForm = ProfForm()
    #plants = SubPlant.objects.all()
    #activeSubscription = Subscription.objects.filter(user=request.user, isActive=True)

    paypal_dict = {
        "business": "receiver_email@example.com",
        "amount": "10000000.00",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": request.build_absolute_uri(reverse('user-profile')),
        "cancel_return": request.build_absolute_uri(reverse('payment-cancle-view')),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)

    return render(request, 'account/profile.html', {'campains': campains,
                                                    'proofs':proofs,
                                                    'profForm':profForm,
                                                    "paypalForm": form
                                                    },) #'plants': plants,'activeSubscription':activeSubscription

from django.contrib import messages
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
def addProf(request):
    if request.method == 'POST':
        profIdEdit = request.POST['id']
        try:
            prof  = Proof.objects.get(pk=profIdEdit)
        except ObjectDoesNotExist:
            prof = None
        profForm = ProfForm(request.POST, request.FILES,instance=prof)
        if profForm.is_valid():

            savedProf = profForm.save(commit=False)
            savedProf.owner = request.user
            savedProf.save()
            if prof == None:
                messages.add_message(request, messages.SUCCESS, 'review added')
            else:
                messages.add_message(request, messages.SUCCESS, 'review updated')
            #print('redirecting')
            #return redirect('/accounts/profile')
        else:
            messages.add_message(request, messages.ERROR, profForm.errors.as_data())
    return redirect('/accounts/profile#reviews')

def delProfView(request, id):
    prof = Proof.objects.get(pk=id)
    if prof.owner == request.user:
        prof.delete()
        messages.add_message(request, messages.SUCCESS, 'prof deleted')
        return redirect('/accounts/profile#reviews')

def delCampainView(request, id):
    camp = Campain.objects.get(pk=id)
    if camp.owner == request.user:
        camp.delete()
        messages.add_message(request, messages.SUCCESS, 'campain deleted')
    return redirect('/accounts/profile#campain')

from django.forms import formset_factory
def profView(request):
    if request.user.is_anonymous:
        return redirect('/accounts/login')
    
    userProofs = Proof.objects.filter(owner=request.user)

    
    return render(request, 'proofs.html', {'proofs':userProofs})
    

def campainView(request, id=-1):
    # redirect the user if not loged in
    if request.user.is_anonymous:
        return redirect('/accounts/login')
    # get camapin to edit or new
    if id == -1:
        camp = None
    else:
        camp = Campain.objects.get(pk=id)


    if request.method == 'POST':
        # save campain
        campainForm = CampainForm(request.POST,instance=camp, user=request.user)
        if campainForm.is_valid():
            campain = campainForm.save(commit=False)
            campain.owner = request.user

            #userSubscriptionPlan = Subscription.objects.filter(user=request.user, isActive=True).first().plant.domain
            activeDomains = Campain.objects.filter(owner=request.user, isActive=True).count()
            #if campain.isActive and userSubscriptionPlan <= activeDomains:
            if False:
                messages.add_message(request, messages.WARNING, 'upgrade your package to activate this campain')
                campain.isActive = False

            campainForm.save()
            if camp == None:
                messages.add_message(request, messages.SUCCESS, 'campain added')
            else:
                messages.add_message(request, messages.SUCCESS, 'campain edited')

            # load profs for the campain
            campainProfs = [i for i in request.POST if i.startswith('profs-checkbox-')]
            campainProfs = map(lambda i: i.replace('profs-checkbox-',''),campainProfs)
            campain.proofs.set(campainProfs)

            if 'save' in request.POST:
                return redirect('/accounts/profile#campain')
            elif 'saveContinue' in request.POST:
                return redirect('/campain/' + str(campainForm.instance.id))
                return HttpResponseRedirect(request.path_info)
            print('redirecting')
        else:
            print(campainForm.errors)
            
    else:
        # send edit campain
        if camp and camp.owner == request.user:
            campainForm = CampainForm(instance=camp, user=request.user)
        # send new campain
        else:
            campainForm = CampainForm(user=request.user)
        
        profs = Proof.objects.filter(owner= request.user)
        return render(request, 'campains.html', {'campainForm':campainForm,
                                                'profs':profs})