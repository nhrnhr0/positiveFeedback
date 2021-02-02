

from django.forms import ModelForm
from .models import Campain

class CampainForm(ModelForm):
    class Meta:
        model = Campain
        fields = '__all__'
        exclude = ['owner', 'proofs']

from .models import Proof
class ProfForm(ModelForm):
    class Meta:
        model = Proof
        fields = '__all__'
        exclude = ['owner',]
