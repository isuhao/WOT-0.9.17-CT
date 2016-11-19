# 2016.11.19 19:51:24 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortOrderInfoWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortOrderInfoWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def as_setWindowDataS(self, data):
        """
        :param data: Represented by FortOrderInfoWindowVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setWindowData(data)

    def as_setDynPropertiesS(self, data):
        """
        :param data: Represented by FortOrderInfoTitleVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDynProperties(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\FortOrderInfoWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:24 Støední Evropa (bìžný èas)
