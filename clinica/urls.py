"""clinica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from users.views import UserViewSet
from cases.views import CaseViewSet
from on_duty.views import OnDutyViewSet
from address.views import AddressViewSet
from axis.views import AxisViewSet
from people.views import PersonViewSet
from attendance.views import AttendanceViewSet
from judicial_appeal.views import JudicialAppealViewSet
from law_suits.views import LawSuitViewSet


router = routers.DefaultRouter()
router.register('accounts', UserViewSet)
router.register('duties', OnDutyViewSet)
router.register('address', AddressViewSet)
router.register('cases', CaseViewSet)
router.register('axes', AxisViewSet)
router.register('people', PersonViewSet)
router.register('attendance', AttendanceViewSet)
router.register('judicial_appeal', JudicialAppealViewSet)
router.register('law_suits', LawSuitViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/login/', obtain_jwt_token),
    path('auth/login/refresh', refresh_jwt_token),
    path('auth/verify-token/', verify_jwt_token)
]
