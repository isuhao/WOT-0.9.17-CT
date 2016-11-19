# 2016.11.19 19:51:19 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/DismissTankmanDialogMeta.py
from gui.Scaleform.daapi.view.dialogs.SimpleDialog import SimpleDialog

class DismissTankmanDialogMeta(SimpleDialog):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SimpleDialog
    """

    def as_tankManS(self, value):
        """
        :param value: Represented by SkillDropModel (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_tankMan(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\DismissTankmanDialogMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:19 Støední Evropa (bìžný èas)
