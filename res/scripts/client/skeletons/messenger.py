# 2016.11.19 19:54:28 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/skeletons/messenger.py


class IMessengerEntry(object):

    @property
    def protos(self):
        raise NotImplementedError

    @property
    def storage(self):
        raise NotImplementedError

    @property
    def gui(self):
        raise NotImplementedError

    def init(self):
        raise NotImplementedError

    def fini(self):
        raise NotImplementedError

    def onAccountShowGUI(self):
        raise NotImplementedError

    def onAvatarInitGUI(self):
        raise NotImplementedError

    def onAvatarShowGUI(self):
        raise NotImplementedError
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\skeletons\messenger.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:54:28 Støední Evropa (bìžný èas)
