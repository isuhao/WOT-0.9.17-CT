# 2016.11.19 19:51:29 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ProfileMeta.py
from gui.Scaleform.framework.entities.View import View

class ProfileMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    """

    def onCloseProfile(self):
        self._printOverrideError('onCloseProfile')

    def as_updateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_update(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\ProfileMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:29 Støední Evropa (bìžný èas)
