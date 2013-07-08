from django.conf.urls import patterns, include, url
from deployments.api import CodeViewSet, DomainViewSet, ApplicationViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'code', CodeViewSet)
router.register(r'domains', DomainViewSet)
router.register(r'applications', ApplicationViewSet)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'monday.views.home', name='home'),
    # url(r'^monday/', include('monday.foo.urls')),

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
