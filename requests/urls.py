from django.conf.urls import url
from . import views

app_name = 'requests'

urlpatterns = [
    url(r'create/$', views.ListRequests.as_view(), name = 'create_request')
]
