from django.conf.urls import url
from . import views

app_name = 'trips'

urlpatterns = [
    url(r'create/$', views.CreateTrip.as_view(), name = 'create_trip'),
    url(r'confirm/(?P<username>[-\w]+)/(?P<pk>\d+)/$', views.TripConfirm.as_view(), name = 'confirm_trip')
]
