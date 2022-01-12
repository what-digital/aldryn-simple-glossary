# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Manager
from django.db.models.query import QuerySet


class GlossaryQuerySet(QuerySet):
    def published(self):
        """
        Returns terms that are published.
        """
        return self.filter(is_published=True)


class GlossaryManager(Manager):
    def get_queryset(self):
        qs = GlossaryQuerySet(self.model, using=self.db)
        return qs

    def published(self):
        return self.get_queryset().published()
