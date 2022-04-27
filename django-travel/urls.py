"""django-travel URL Configuration

The `urlpatterns` list route URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from comment.views import AttractionCommentMappingView
from route.views import RouteViewSet, RouteAttractionMappingView
from attraction.views import AttractionViewSet

router = DefaultRouter()
router.register('route', RouteViewSet)
router.register('attraction', AttractionViewSet)

urlpatterns = [

]
urlpatterns += router.urls
urlpatterns = [
    re_path('^', include(router.urls)),
    path('route_Attraction/', RouteAttractionMappingView.as_view(), name='route_attraction'),
    url(r'attraction_comment/(.+)', AttractionCommentMappingView.as_view(), name='attraction_comment'),
    path('admin/', admin.site.urls),
]
