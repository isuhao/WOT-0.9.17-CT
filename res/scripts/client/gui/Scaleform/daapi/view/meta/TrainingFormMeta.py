# 2016.11.19 19:51:35 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TrainingFormMeta.py
from gui.Scaleform.framework.entities.View import View

class TrainingFormMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    """

    def joinTrainingRequest(self, id):
        self._printOverrideError('joinTrainingRequest')

    def createTrainingRequest(self):
        self._printOverrideError('createTrainingRequest')

    def onEscape(self):
        self._printOverrideError('onEscape')

    def onLeave(self):
        self._printOverrideError('onLeave')

    def as_setListS(self, data):
        """
        :param data: Represented by TrainingFormVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setList(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\TrainingFormMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:35 Støední Evropa (bìžný èas)
