"""
Topics Apps
"""
###
# Libraries
###
from django.apps import AppConfig


###
# Config
###
class TopicsConfig(AppConfig):
    name = 'topics'

    def ready(self):
        import topics.signals
