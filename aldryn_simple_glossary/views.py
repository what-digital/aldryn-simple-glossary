# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView

from .models import Term


class GlossaryListView(ListView):
    model = Term
    template_name = 'aldryn_simple_glossary/terms_list.html'

    def get_queryset(self):
        qs = super(GlossaryListView, self).get_queryset()
        return qs.published()
