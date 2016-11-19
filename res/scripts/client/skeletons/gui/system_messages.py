# 2016.11.19 19:54:29 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/skeletons/gui/system_messages.py


class ISystemMessages(object):

    def init(self):
        raise NotImplementedError

    def destroy(self):
        raise NotImplementedError

    def pushMessage(self, text, type, priority = None):
        raise NotImplementedError

    def pushI18nMessage(self, key, *args, **kwargs):
        raise NotImplementedError
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\skeletons\gui\system_messages.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:54:29 Støední Evropa (bìžný èas)
