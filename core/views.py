from django.shortcuts import render
from django.http import HttpResponse

from core.models import Campain, Proof



# Create your views here.
def generateReview(reuqest, id):
    print(id)
    campain = Campain.objects.get(pk=id)

    return render(request=reuqest, content_type="application/javascript",template_name='reviews.loader.js',   context={"campain":campain})
    #return HttpResponse("console.log('hey');", 

def testIndexView(request):
    return render(request, 'index.html' , {})


from .forms import CampainForm
def profileView(request):
    campains = Campain.objects.filter(owner=request.user)
    

    return render(request, 'account/profile.html', {'campains': campains})

from django.contrib import messages
from django.shortcuts import redirect

def delCampainView(request, id):
    camp = Campain.objects.get(pk=id)
    if camp.owner == request.user:
        camp.delete()
        messages.add_message(request, messages.SUCCESS, 'campain deleted')
    return redirect('/accounts/profile')
def campainView(request, id=-1):
    if id == -1:
        camp = None
    else:
        camp = Campain.objects.get(pk=id)


    if request.method == 'POST':
        campainForm = CampainForm(request.POST,instance=camp)
        if campainForm.is_valid():
            campain = campainForm.save(commit=False)
            campain.owner = request.user
            campainForm.save()
            messages.add_message(request, messages.SUCCESS, 'campain added')
            print('redirecting')
            return redirect('/accounts/profile')
    else:
        if camp and camp.owner == request.user:
            campainForm = CampainForm(instance=camp)
        else:
            campainForm = CampainForm()
        return render(request, 'campains.html', {'campainForm':campainForm})