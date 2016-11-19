# 2016.11.19 19:51:25 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/IconDialogMeta.py
from gui.Scaleform.daapi.view.dialogs.SimpleDialog import SimpleDialog

class IconDialogMeta(SimpleDialog):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SimpleDialog
    """

    def as_setIconS(self, path):
        if self._isDAAPIInited():
            return self.flashObject.as_setIcon(path)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\IconDialogMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:25 Støední Evropa (bìžný èas)
