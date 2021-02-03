from django.db import models
from colorfield.fields import ColorField
from django.utils.translation import gettext as _
from django.conf import settings

# Create your models here.


class Proof(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        #null=True,blank=True,
    )
    image = models.ImageField(upload_to="proofs", blank=True, null=True)
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

    
    SLIDE_IN_RIGHT = 'slide_right'
    SLIDE_IN_LEFT = 'slide_left'
    SLIDE_IN_BOTTOM = 'slide_bottom'
    TRANSITION_IN_CHOICES = [
        (SLIDE_IN_RIGHT, 'slide in right'),
        (SLIDE_IN_LEFT, 'slide in left'),
        (SLIDE_IN_BOTTOM, 'slide in bottom'),
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

    DIR_LTR = 'ltr'
    DIR_RTL = 'rtl'
    DIRECTION_CHOICES = [
        (DIR_LTR, 'left to right'),
        (DIR_RTL, 'right to left'),
    ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)#,null=True,blank=True,)
    name = models.CharField(blank=False, verbose_name=_('name'), max_length=120)
    isActive = models.BooleanField(verbose_name="active", default=False)
    url = models.URLField(verbose_name="url")
    direction = models.CharField(max_length=3, choices=DIRECTION_CHOICES, default=DIR_LTR)

    startDelay = models.IntegerField(verbose_name="start delay", default=5)
    displayTime = models.IntegerField(verbose_name="display time", default=10)
    hideTime = models.IntegerField(verbose_name="hide time", default=4)


    layout = models.CharField(max_length=1, choices=LAYOUT_CHOICES, default=BIG_CIRCLE_IMAGE)
    transitionIn = models.CharField(max_length=20, choices=TRANSITION_IN_CHOICES, default=SLIDE_IN_RIGHT)
    transitionOut = models.CharField(max_length=1, choices=TRANSITION_OUT_CHOICES, default=SLIDE_OUT)

    position = models.CharField(max_length=1, choices=POSITION_CHOICES, default=LEFT_BOTTOM)
    xOffset = models.CharField(max_length=20, default="10px")
    yOffset = models.CharField(max_length=20, default="20px")


    backgroundColor = ColorField(default="#ffffff")
    headingColor = ColorField(default="#000000")
    textColor = ColorField(default="#333333")
    customCSS = models.TextField(verbose_name="custom css", blank=True)

    proofs = models.ManyToManyField(to=Proof, related_name='camp')
