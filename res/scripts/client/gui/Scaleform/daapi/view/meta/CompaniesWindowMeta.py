# 2016.11.19 19:51:16 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CompaniesWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class CompaniesWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def createCompany(self):
        self._printOverrideError('createCompany')

    def joinCompany(self, prbID):
        self._printOverrideError('joinCompany')

    def getDivisionsList(self):
        self._printOverrideError('getDivisionsList')

    def refreshCompaniesList(self, creatorMask, isNotInBattle, division):
        self._printOverrideError('refreshCompaniesList')

    def requestPlayersList(self, prbID):
        self._printOverrideError('requestPlayersList')

    def showFAQWindow(self):
        self._printOverrideError('showFAQWindow')

    def getClientID(self):
        self._printOverrideError('getClientID')

    def as_getCompaniesListDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getCompaniesListDP()

    def as_showPlayersListS(self, index):
        if self._isDAAPIInited():
            return self.flashObject.as_showPlayersList(index)

    def as_setDefaultFilterS(self, creatorMask, isNotInBattle, division):
        if self._isDAAPIInited():
            return self.flashObject.as_setDefaultFilter(creatorMask, isNotInBattle, division)

    def as_setRefreshCoolDownS(self, time):
        if self._isDAAPIInited():
            return self.flashObject.as_setRefreshCoolDown(time)

    def as_disableCreateButtonS(self, isDisable):
        if self._isDAAPIInited():
            return self.flashObject.as_disableCreateButton(isDisable)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\CompaniesWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:16 St�edn� Evropa (b�n� �as)
