# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class SimpleGlossaryApp(CMSApp):
    app_name = 'simple_glossary'
    name = _('Simple glossary')
    urls = ['aldryn_simple_glossary.urls']

    def get_urls(self, page=None, language=None, **kwargs):
        return ['aldryn_simple_glossary.urls']


apphook_pool.register(SimpleGlossaryApp)

