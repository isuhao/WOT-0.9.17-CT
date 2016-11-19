# 2016.11.19 19:51:41 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/AbstractViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class AbstractViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def onFocusIn(self, alias):
        self._printOverrideError('onFocusIn')

    def as_setupContextHintBuilderS(self, builderLnk, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setupContextHintBuilder(builderLnk, data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\framework\entities\abstract\AbstractViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:41 Støední Evropa (bìžný èas)
