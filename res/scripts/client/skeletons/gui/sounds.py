# 2016.11.19 19:54:29 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/skeletons/gui/sounds.py


class ISoundsController(object):

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError

    def stop(self, isDisconnected = False):
        raise NotImplementedError

    @property
    def system(self):
        raise NotImplementedError

    def enable(self):
        raise NotImplementedError

    def disable(self):
        raise NotImplementedError

    def isEnabled(self):
        raise NotImplementedError
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\skeletons\gui\sounds.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:54:29 Støední Evropa (bìžný èas)
