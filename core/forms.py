

from django.forms import ModelForm, FloatField, NumberInput
from .models import Campain
from subscriptions.models import Subscription
class CampainForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super(CampainForm, self).__init__(*args, **kwargs)
        if Subscription.objects.get(user=self.user, isActive=True).plant.name == 'starter':            
            self.fields['direction'].widget.attrs['disabled'] = 'disabled'
            self.fields['layout'].widget.attrs['disabled'] = 'disabled'
            self.fields['transitionIn'].widget.attrs['disabled'] = 'disabled'
            self.fields['transitionOut'].widget.attrs['disabled'] = 'disabled'
            self.fields['position'].widget.attrs['disabled'] = 'disabled'
            self.fields['xOffset'].widget.attrs['disabled'] = 'disabled'
            self.fields['yOffset'].widget.attrs['disabled'] = 'disabled'
            self.fields['backgroundColor'].widget.attrs['disabled'] = 'disabled'
            self.fields['headingColor'].widget.attrs['disabled'] = 'disabled'
            self.fields['backgroundColor'].widget.attrs['readonly'] = True
            self.fields['headingColor'].widget.attrs['readonly'] = True

        print('CampainForm __init__')
        
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
