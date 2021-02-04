

from django.forms import ModelForm, FloatField, NumberInput
from .models import Campain

class CampainForm(ModelForm):
    class Meta:
        model = Campain
        fields = '__all__'
        exclude = ['owner', 'proofs']

from .models import Proof
class ProfForm(ModelForm):
    stars = FloatField(required=False, max_value=5, min_value=-1,initial=4.5,label="stars (-1 = deactivate)",
        widget=NumberInput(attrs={'id': 'form_starts', 'step': '0.5'}))
    class Meta:
        model = Proof
        fields = '__all__'
        exclude = ['owner',]
