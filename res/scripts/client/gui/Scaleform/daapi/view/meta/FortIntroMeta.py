# 2016.11.19 19:51:23 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortIntroMeta.py
from gui.Scaleform.daapi.view.lobby.rally.BaseRallyIntroView import BaseRallyIntroView

class FortIntroMeta(BaseRallyIntroView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseRallyIntroView
    """

    def as_setIntroDataS(self, data):
        """
        :param data: Represented by IntroViewVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setIntroData(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\FortIntroMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:23 Støední Evropa (bìžný èas)
