from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from especies import views

router = routers.DefaultRouter()
router.register(r'especies', views.EspecieViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^especies/', include('especies.urls')),
    url(r'^admin/', admin.site.urls),
]
