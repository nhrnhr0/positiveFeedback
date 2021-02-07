from django.contrib import admin
from .models import SubPlant, Subscription, SubPlantFeature
# Register your models here.
class SubPlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'domain',)
admin.site.register(SubPlant,SubPlantAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('plant', 'user', 'isActive', 'isCanceled', 'start_time', 'end_time', 'created_at', 'last_updated_on')
admin.site.register(Subscription, SubscriptionAdmin)

class SubPlantFeatureAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(SubPlantFeature, SubPlantFeatureAdmin)