# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from djangocms_text_ckeditor.fields import HTMLField

from .managers import GlossaryManager


class Term(models.Model):

    title = models.CharField(
        _('Title'),
        max_length=255,
        help_text=_("Glossary term title"),

    )
    description = HTMLField(_('Term description'), default='')
    is_published = models.BooleanField(_("is published"), default=False)

    user = models.ForeignKey(
        getattr(settings, 'AUTH_USER_MODEL', 'auth.User'),
        null=True, blank=True, related_name='terms', on_delete=models.SET_NULL)
    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)

    objects = GlossaryManager()

    def __str__(self):
        return self.title

    def first_letter(self):
        return self.title[0].capitalize()

    class Meta:
        ordering = ['title']
