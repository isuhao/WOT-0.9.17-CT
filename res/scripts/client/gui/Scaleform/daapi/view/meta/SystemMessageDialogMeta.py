# 2016.11.19 19:51:35 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/SystemMessageDialogMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class SystemMessageDialogMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def as_setInitDataS(self, value):
        """
        :param value: Represented by NotificationDialogInitInfoVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(value)

    def as_setMessageDataS(self, value):
        """
        :param value: Represented by NotificationInfoVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setMessageData(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\SystemMessageDialogMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:35 Støední Evropa (bìžný èas)
