# 2016.11.19 19:52:32 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/server_events/__init__.py
from gui.server_events.EventsCache import EventsCache
from skeletons.gui.server_events import IEventsCache
__all__ = ('getServerEventsConfig',)

def getServerEventsConfig(manager):
    """ Configures services for package server_events.
    :param manager: helpers.dependency.DependencyManager
    """
    cache = EventsCache()
    cache.init()
    manager.bindInstance(IEventsCache, cache, finalizer='fini')
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\server_events\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:52:32 Støední Evropa (bìžný èas)
