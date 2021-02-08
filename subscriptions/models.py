from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class SubPlant(models.Model):
    domain = models.SmallIntegerField(verbose_name="number of domains")
    price = models.DecimalField(verbose_name="price", max_digits=5, decimal_places=2,)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SubPlantFeature(models.Model):
    subPlant = models.ManyToManyField(to=SubPlant, related_name='features')
    title = models.CharField(max_length=150)

class Subscription(models.Model):
    plant = models.ForeignKey(to=SubPlant, on_delete=models.CASCADE) 
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    isActive = models.BooleanField(verbose_name="is active")
    isCanceled = models.BooleanField(verbose_name="is cancle")
    start_time = models.DateTimeField() 
    end_time = models.DateTimeField()
    created_at = models.DateTimeField()
    last_updated_on =  models.DateTimeField()

    def __str__(self):
        return self.user.first_name +'>'+ str(self.plant) + ' : ' + str(self.isActive)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.last_updated_on = timezone.now()
        return super(Subscription, self).save(*args, **kwargs)

from django.contrib.auth.models import User

#class Profile(models.Model):
#    user = models.OneToOneField(to=User, on_delete=models.CASCADE)

