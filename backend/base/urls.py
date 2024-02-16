from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ac_app', views.Ac_appViewSet, basename='ac_app')

urlpatterns = [
    
]

urlpatterns += router.urls