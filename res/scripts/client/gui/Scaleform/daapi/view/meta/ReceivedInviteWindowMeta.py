# 2016.11.19 19:51:31 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ReceivedInviteWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ReceivedInviteWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def acceptInvite(self):
        self._printOverrideError('acceptInvite')

    def declineInvite(self):
        self._printOverrideError('declineInvite')

    def cancelInvite(self):
        self._printOverrideError('cancelInvite')

    def as_setTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setTitle(value)

    def as_setReceivedInviteInfoS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setReceivedInviteInfo(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\ReceivedInviteWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:31 St�edn� Evropa (b�n� �as)
