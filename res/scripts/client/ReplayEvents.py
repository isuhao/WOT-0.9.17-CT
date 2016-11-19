# 2016.11.19 19:47:09 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/ReplayEvents.py
import Event

class _ReplayEvents(object):

    def __init__(self):
        self.onTimeWarpStart = Event.Event()
        self.onTimeWarpFinish = Event.Event()
        self.onPause = Event.Event()
        self.onMuteSound = Event.Event()
        self.onWatcherNotify = Event.Event()


g_replayEvents = _ReplayEvents()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\ReplayEvents.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:47:09 Støední Evropa (bìžný èas)
