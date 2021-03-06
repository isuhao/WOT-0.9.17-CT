# 2016.11.19 19:51:15 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanInvitesWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ClanInvitesWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def onInvitesButtonClick(self):
        self._printOverrideError('onInvitesButtonClick')

    def as_setDataS(self, data):
        """
        :param data: Represented by ClanInvitesWindowVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_setClanInfoS(self, data):
        """
        :param data: Represented by ClanBaseInfoVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClanInfo(data)

    def as_setHeaderStateS(self, data):
        """
        :param data: Represented by ClanInvitesWindowHeaderStateVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderState(data)

    def as_setClanEmblemS(self, source):
        if self._isDAAPIInited():
            return self.flashObject.as_setClanEmblem(source)

    def as_setControlsEnabledS(self, enabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setControlsEnabled(enabled)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\ClanInvitesWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:15 St�edn� Evropa (b�n� �as)
