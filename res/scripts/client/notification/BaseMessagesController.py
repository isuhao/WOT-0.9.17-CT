# 2016.11.19 19:54:22 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/notification/BaseMessagesController.py


class BaseMessagesController(object):

    def __init__(self, model):
        self._model = model

    def cleanUp(self):
        self._model = None
        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\notification\BaseMessagesController.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:54:22 Støední Evropa (bìžný èas)
