# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from cms.admin.placeholderadmin import FrontendEditableAdminMixin
from .models import Term


class TermAdmin(FrontendEditableAdminMixin,
                admin.ModelAdmin):
    model = Term
    list_display = (
        'title',
        'is_published',
    )
    list_filter = ['is_published', 'user']
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at', 'user')
    fieldsets = (
        (None, {
           'fields': (
               'title',
               'description',
               'is_published',
           )
        }),
        (_('Meta information'), {
            'classes': ('collapse',),
            'fields': (
                'user',
                'created_at',
                'updated_at',
            )
        }),
    )

    def save_model(self, request, obj, form, change):
        # set the current user as author
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        return super(TermAdmin, self).save_model(request, obj, form, change)


admin.site.register(Term, TermAdmin)
