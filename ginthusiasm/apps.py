from __future__ import unicode_literals

from django.apps import AppConfig

class GinthusiasmConfig(AppConfig):
    name = 'ginthusiasm'

    def ready(self):
        import ginthusiasm.signals
