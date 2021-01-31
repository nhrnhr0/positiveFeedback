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

