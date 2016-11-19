# 2016.11.19 19:51:35 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TankmanOperationDialogMeta.py
from gui.Scaleform.daapi.view.dialogs.SimpleDialog import SimpleDialog

class TankmanOperationDialogMeta(SimpleDialog):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SimpleDialog
    """

    def as_setDataS(self, data):
        """
        :param data: Represented by TankmanOperationDialogVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\TankmanOperationDialogMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:35 Støední Evropa (bìžný èas)
