# 2016.11.19 19:51:21 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortCalendarWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortCalendarWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def as_updatePreviewDataS(self, data):
        """
        :param data: Represented by FortCalendarPreviewBlockVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updatePreviewData(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\FortCalendarWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:21 Støední Evropa (bìžný èas)
