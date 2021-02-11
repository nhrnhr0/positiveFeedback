"""webReviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from core.views import testIndexView,generateReview ,profileView, campainView,delCampainView, profView, addProf,delProfView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test', testIndexView),
    path('load-campain/<int:id>', generateReview),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', profileView, name='user-profile'),
    path('accounts/profile/<int:review>', profileView),
    path('campain/', campainView),
    path('campain/<int:id>', campainView),
    path('campain/del/<int:id>/', delCampainView),
    #path('prof/', profView),
    path('prof/del/<int:id>/', delProfView),
    path('addProf', addProf),
    re_path('^paypal/', include('paypal.standard.ipn.urls')),
    path('payment-cancle', testIndexView,name='payment-cancle-view'),
]
if settings.DEBUG:
    urlpatterns= urlpatterns + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
    urlpatterns= urlpatterns + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    