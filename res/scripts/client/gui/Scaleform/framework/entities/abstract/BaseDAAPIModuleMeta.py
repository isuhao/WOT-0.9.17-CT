# 2016.11.19 19:51:41 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/BaseDAAPIModuleMeta.py
from gui.Scaleform.framework.entities.DAAPIEntity import DAAPIEntity

class BaseDAAPIModuleMeta(DAAPIEntity):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends DAAPIEntity
    """

    def as_populateS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_populate()

    def as_disposeS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_dispose()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\framework\entities\abstract\BaseDAAPIModuleMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:41 Støední Evropa (bìžný èas)
