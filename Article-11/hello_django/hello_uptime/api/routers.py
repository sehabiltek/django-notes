from rest_framework import routers

from hello_uptime.api import views

uptime_router = routers.DefaultRouter()
uptime_router.register('monitor', viewset=views.MonitorViewSet, base_name='monitor')
