# 2016.11.19 19:51:22 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortFixedPlayersWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortFixedPlayersWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def assignToBuilding(self):
        self._printOverrideError('assignToBuilding')

    def as_setWindowTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setWindowTitle(value)

    def as_setDataS(self, data):
        """
        :param data: Represented by FortFixedPlayersVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\FortFixedPlayersWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:22 Støední Evropa (bìžný èas)
