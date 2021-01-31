from django.contrib import admin

from .models import Campain, Proof
# Register your models here.
class CampainAdmin(admin.ModelAdmin):
    list_display= ('isActive', 'name', 'url','startDelay','displayTime','hideTime', 'layout', 'transitionIn', 'transitionOut', 'position',
                    'xOffset', 'yOffset', 'backgroundColor', 'headingColor', 'textColor',
                    'customCSS')
    list_display_links= ('name',)
    
admin.site.register(Campain,CampainAdmin)



class ProofAdmin(admin.ModelAdmin):
    list_display = ('title', 'time', 'message', 'logo')
admin.site.register(Proof,ProofAdmin)