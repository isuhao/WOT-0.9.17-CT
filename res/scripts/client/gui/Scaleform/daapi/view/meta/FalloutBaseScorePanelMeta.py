# 2016.11.19 19:51:20 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FalloutBaseScorePanelMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FalloutBaseScorePanelMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def as_initS(self, maxValue, warningValue):
        if self._isDAAPIInited():
            return self.flashObject.as_init(maxValue, warningValue)

    def as_playScoreHighlightAnimS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_playScoreHighlightAnim()

    def as_stopScoreHighlightAnimS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_stopScoreHighlightAnim()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\FalloutBaseScorePanelMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:20 Støední Evropa (bìžný èas)
