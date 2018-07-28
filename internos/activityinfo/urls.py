from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.IndexView.as_view(),
        name='home'
    ),

    url(
        regex=r'^activityinfo-export/$',
        view=views.ExportViewSet.as_view(),
        name='export'
    ),
]
