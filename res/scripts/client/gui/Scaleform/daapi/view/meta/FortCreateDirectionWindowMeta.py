# 2016.11.19 19:51:22 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortCreateDirectionWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortCreateDirectionWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def openNewDirection(self):
        self._printOverrideError('openNewDirection')

    def closeDirection(self, id):
        self._printOverrideError('closeDirection')

    def as_setDescriptionS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setDescription(value)

    def as_setupButtonS(self, enabled, visible, tooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_setupButton(enabled, visible, tooltip)

    def as_setDirectionsS(self, data):
        """
        :param data: Represented by Vector.<DirectionVO> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setDirections(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\FortCreateDirectionWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:22 Støední Evropa (bìžný èas)
