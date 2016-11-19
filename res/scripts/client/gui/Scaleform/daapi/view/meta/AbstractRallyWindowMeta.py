# 2016.11.19 19:51:11 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AbstractRallyWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class AbstractRallyWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def canGoBack(self):
        self._printOverrideError('canGoBack')

    def onBrowseRallies(self):
        self._printOverrideError('onBrowseRallies')

    def onBrowseStaticsRallies(self):
        self._printOverrideError('onBrowseStaticsRallies')

    def onCreateRally(self):
        self._printOverrideError('onCreateRally')

    def onJoinRally(self, rallyId, slotIndex, peripheryId):
        self._printOverrideError('onJoinRally')

    def as_loadViewS(self, flashAlias, pyAlias):
        if self._isDAAPIInited():
            return self.flashObject.as_loadView(flashAlias, pyAlias)

    def as_enableWndCloseBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_enableWndCloseBtn(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\AbstractRallyWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:11 Støední Evropa (bìžný èas)
