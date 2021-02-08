

from django.forms import ModelForm, FloatField, NumberInput
from .models import Campain
from subscriptions.models import Subscription
from django import forms
from django.forms.widgets import TextInput
from colorfield.fields import ColorField
class CampainForm(ModelForm):
    
    def __init__(self, user, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super(CampainForm, self).__init__(*args, **kwargs)
        self.user = user
        if Subscription.objects.get(user=self.user, isActive=True).plant.name == 'starter' or \
            Subscription.objects.get(user=self.user, isActive=True).plant.name == 'Trail':
            #self.fields['position'].widget.attrs['readonly'] = True
            self.fields['xOffset'].widget.attrs['readonly'] = True
            self.fields['yOffset'].widget.attrs['readonly'] = True

            self.fields['position'].widget.attrs['disabled '] = True
            self.fields['direction'].widget.attrs['disabled '] = True
            self.fields['layout'].widget.attrs['disabled '] = True
            self.fields['transitionIn'].widget.attrs['disabled '] = True
            self.fields['transitionOut'].widget.attrs['disabled '] =True

            self.fields['backgroundColor'].widget.attrs['disabled '] = True
            self.fields['headingColor'].widget.attrs['disabled '] = True
            self.fields['textColor'].widget.attrs['disabled '] =True

            self.fields['position'].required = False
            self.fields['direction'].required = False
            self.fields['layout'].required = False
            self.fields['transitionIn'].required = False
            self.fields['transitionOut'].required = False
            self.fields['backgroundColor'].required = False
            self.fields['headingColor'].required = False
            self.fields['textColor'].required = False


            #self.fields['backgroundColor'].widget.attrs['disabled'] = 'disabled'
            #self.fields['headingColor'].widget.attrs['disabled'] = 'disabled'
            #self.fields['backgroundColor'].widget.attrs['readonly'] = True
            #self.fields['headingColor'].widget.attrs['readonly'] = True
        
    #backgroundColor = ColorField(forma)
    backgroundColor = TextInput(attrs={'type':'color'})
    class Meta:
        model = Campain
        fields = '__all__'
        exclude = ['owner', 'proofs']
        widgets = {
                   'backgroundColor': TextInput(attrs={'type': 'color'}),
                   'headingColor': TextInput(attrs={'type': 'color'}),
                   'textColor': TextInput(attrs={'type': 'color'}),
                   }


from .models import Proof
class ProfForm(ModelForm):
    stars = FloatField(required=False, max_value=5, min_value=-1,initial=4.5,label="stars (-1 = deactivate)",
        widget=NumberInput(attrs={'id': 'form_starts', 'step': '0.5'}))
    class Meta:
        model = Proof
        fields = '__all__'
        exclude = ['owner',]
