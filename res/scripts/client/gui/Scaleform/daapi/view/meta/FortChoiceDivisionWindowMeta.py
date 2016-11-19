# 2016.11.19 19:51:21 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortChoiceDivisionWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortChoiceDivisionWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def selectedDivision(self, divisionID):
        self._printOverrideError('selectedDivision')

    def changedDivision(self, divisionID):
        self._printOverrideError('changedDivision')

    def as_setDataS(self, data):
        """
        :param data: Represented by FortChoiceDivisionVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\FortChoiceDivisionWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:21 Støední Evropa (bìžný èas)
