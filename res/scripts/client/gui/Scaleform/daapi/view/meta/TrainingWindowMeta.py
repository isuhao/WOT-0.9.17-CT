# 2016.11.19 19:51:36 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TrainingWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class TrainingWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def updateTrainingRoom(self, key, time, isPrivate, description):
        self._printOverrideError('updateTrainingRoom')

    def as_setDataS(self, info, mapsData):
        """
        :param info: Represented by TrainingWindowVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(info, mapsData)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\TrainingWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:36 St�edn� Evropa (b�n� �as)
