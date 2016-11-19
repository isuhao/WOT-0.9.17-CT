# 2016.11.19 19:51:22 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortDisableDefencePeriodWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortDisableDefencePeriodWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def onClickApplyButton(self):
        self._printOverrideError('onClickApplyButton')

    def as_setDataS(self, data):
        """
        :param data: Represented by DisableDefencePeriodVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\FortDisableDefencePeriodWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:22 Støední Evropa (bìžný èas)
