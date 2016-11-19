# 2016.11.19 19:51:41 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/abstract/EventLogManagerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIModule import BaseDAAPIModule

class EventLogManagerMeta(BaseDAAPIModule):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIModule
    """

    def logEvent(self, subSystemType, eventType, uiid, arg):
        self._printOverrideError('logEvent')

    def as_setSystemEnabledS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setSystemEnabled(isEnabled)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\framework\entities\abstract\EventLogManagerMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:41 Støední Evropa (bìžný èas)
