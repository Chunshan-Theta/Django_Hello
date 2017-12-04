"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from APP1.views import hello_world
from APP1.views import YoutubeDownload
from BSA.views import Cal_BSA
from BSA.views import BSA_sample
from BSA.views import catch_from_SQL
from BSA.views import BehaviorList
from BSA.views import BehaviorAllList
from BSA.views import Catch_From_DB_to_BSA
from BSA.views import API_BSA_Json
from BSA.views import draw_ZScore
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', hello_world),
    url(r'^YoutubeDownload/(?P<Url>\S*)/$', YoutubeDownload),
    url(r'^YoutubeDownload/$', YoutubeDownload),
    url(r'^BSA/$', Cal_BSA),
    url(r'^BSA_Sample/', BSA_sample),
    url(r'^BSA_SQLData/', catch_from_SQL),
    url(r'^BSA_BList/(?P<stu_id>\S*)/$', BehaviorList),
    url(r'^BSA_BList/$', BehaviorAllList),
    url(r'^BSA_BArray/$', Catch_From_DB_to_BSA),
    url(r'^BSA_BArray/(?P<num>\S*)/(?P<group>\S*)/$', Catch_From_DB_to_BSA),
    url(r'^BSA_API_Json/(?P<ApiType>\S*)/(?P<num>\S*)/(?P<group>\S*)/$', API_BSA_Json),
    url(r'^BSA_API_Json/(?P<num>\S*)/(?P<group>\S*)/$', API_BSA_Json),
    url(r'^BSA_API_Json/$', API_BSA_Json),
    url(r'^BSA/draw/$',draw_ZScore)
]
