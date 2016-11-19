# 2016.11.19 19:51:17 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/CrewOperationsPopOverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class CrewOperationsPopOverMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    """

    def invokeOperation(self, operationName):
        self._printOverrideError('invokeOperation')

    def as_updateS(self, data):
        """
        :param data: Represented by CrewOperationsInitVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_update(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\CrewOperationsPopOverMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:17 Støední Evropa (bìžný èas)
