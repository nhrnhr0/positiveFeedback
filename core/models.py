from django.db import models
from colorfield.fields import ColorField
from django.utils.translation import gettext as _

# Create your models here.


class Proof(models.Model):
    image = models.ImageField(upload_to="proofs")
    title = models.CharField(max_length=80)
    time = models.CharField(max_length=50, blank=True)
    message = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="logos", blank=True)

    def __str__(self):
        return self.title
    
    
class Campain(models.Model):
    BIG_CIRCLE_IMAGE = '0'
    LAYOUT_CHOICES = [
        (BIG_CIRCLE_IMAGE, 'big circle image'),
    ]

    SLIDE_IN = '0'
    TRANSITION_IN_CHOICES = [
        (SLIDE_IN, 'slide in'),
    ]

    SLIDE_OUT = '0'
    TRANSITION_OUT_CHOICES = [
        (SLIDE_OUT, 'slide out'),
    ]

    LEFT_BOTTOM = '0'
    LEFT_TOP = '1'
    RIGHT_BOTTOM = '2'
    RIGHT_TOP = '3'
    POSITION_CHOICES = [
        (LEFT_BOTTOM, 'left bottom'),
        (LEFT_TOP, 'left top'),
        (RIGHT_BOTTOM, 'right bottom'),
        (RIGHT_TOP, 'right top'),
    ]
    name = models.CharField(blank=False, verbose_name=_('name'), max_length=120)
    isActive = models.BooleanField(verbose_name="active", default=False)
    url = models.URLField(verbose_name="url")

    startDelay = models.IntegerField(verbose_name="start delay", default=5)
    displayTime = models.IntegerField(verbose_name="display time", default=10)
    hideTime = models.IntegerField(verbose_name="hide time", default=4)


    layout = models.CharField(max_length=1, choices=LAYOUT_CHOICES, default=BIG_CIRCLE_IMAGE)
    transitionIn = models.CharField(max_length=1, choices=TRANSITION_IN_CHOICES, default=SLIDE_IN)
    transitionOut = models.CharField(max_length=1, choices=TRANSITION_OUT_CHOICES, default=SLIDE_OUT)

    position = models.CharField(max_length=1, choices=POSITION_CHOICES, default=LEFT_BOTTOM)
    xOffset = models.CharField(max_length=20, default="10px")
    yOffset = models.CharField(max_length=20, default="20px")


    backgroundColor = ColorField(default="#ffffff")
    headingColor = ColorField(default="#000000")
    textColor = ColorField(default="#333333")
    customCSS = models.TextField(verbose_name="custom css", blank=True)

    proofs = models.ManyToManyField(to=Proof)
