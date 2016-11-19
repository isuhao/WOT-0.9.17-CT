# 2016.11.19 19:51:33 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/StaticFormationInvitesAndRequestsMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class StaticFormationInvitesAndRequestsMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def setDescription(self, value):
        self._printOverrideError('setDescription')

    def setShowOnlyInvites(self, value):
        self._printOverrideError('setShowOnlyInvites')

    def resolvePlayerRequest(self, playerId, playerAccepted):
        self._printOverrideError('resolvePlayerRequest')

    def as_getDataProviderS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDataProvider()

    def as_setStaticDataS(self, data):
        """
        :param data: Represented by InvitesAndRequestsVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setStaticData(data)

    def as_setTeamDescriptionS(self, description):
        if self._isDAAPIInited():
            return self.flashObject.as_setTeamDescription(description)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\StaticFormationInvitesAndRequestsMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:33 Støední Evropa (bìžný èas)
