# 2016.11.19 19:51:15 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanInvitesWindowAbstractTabViewMeta.py
from gui.Scaleform.daapi.view.lobby.clans.invites.ClanInvitesViewWithTable import ClanInvitesViewWithTable

class ClanInvitesWindowAbstractTabViewMeta(ClanInvitesViewWithTable):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends ClanInvitesViewWithTable
    """

    def filterBy(self, filterName):
        self._printOverrideError('filterBy')

    def as_updateFilterStateS(self, data):
        """
        :param data: Represented by ClanInvitesWindowTableFilterVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateFilterState(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\ClanInvitesWindowAbstractTabViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:15 Støední Evropa (bìžný èas)
