# 2016.11.19 19:54:29 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/skeletons/gui/prb_control.py


class IPrbControlLoader(object):
    __slots__ = ()

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def getDispatcher(self):
        raise NotImplementedError

    def getInvitesManager(self):
        raise NotImplementedError

    def getAutoInvitesNotifier(self):
        raise NotImplementedError

    def getPeripheriesHandler(self):
        raise NotImplementedError

    def getStorage(self):
        raise NotImplementedError

    def isEnabled(self):
        raise NotImplementedError

    def setEnabled(self, enabled):
        raise NotImplementedError

    def onAccountShowGUI(self, ctx):
        raise NotImplementedError

    def onAvatarBecomePlayer(self):
        raise NotImplementedError

    def onDisconnected(self):
        raise NotImplementedError
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\skeletons\gui\prb_control.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:54:29 Støední Evropa (bìžný èas)
