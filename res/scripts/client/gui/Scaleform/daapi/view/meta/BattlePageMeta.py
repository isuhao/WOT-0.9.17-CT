# 2016.11.19 19:51:13 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/BattlePageMeta.py
from gui.Scaleform.framework.entities.View import View

class BattlePageMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    """

    def as_checkDAAPIS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_checkDAAPI()

    def as_setPostmortemTipsVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPostmortemTipsVisible(value)

    def as_setComponentsVisibilityS(self, visible, hidden):
        """
        :param visible: Represented by Vector.<String> (AS)
        :param hidden: Represented by Vector.<String> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setComponentsVisibility(visible, hidden)

    def as_isComponentVisibleS(self, componentKey):
        if self._isDAAPIInited():
            return self.flashObject.as_isComponentVisible(componentKey)

    def as_getComponentsVisibilityS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getComponentsVisibility()

    def as_toggleCtrlPressFlagS(self, isCtrlPressed):
        if self._isDAAPIInited():
            return self.flashObject.as_toggleCtrlPressFlag(isCtrlPressed)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\BattlePageMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:13 Støední Evropa (bìžný èas)
