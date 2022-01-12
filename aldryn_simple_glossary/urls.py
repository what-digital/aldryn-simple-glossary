# -*- coding: utf-8 -*-
from django.conf.urls import url

from .views import GlossaryListView

urlpatterns = [
    url(r'^$', GlossaryListView.as_view(), name='glossary-list'),
]
