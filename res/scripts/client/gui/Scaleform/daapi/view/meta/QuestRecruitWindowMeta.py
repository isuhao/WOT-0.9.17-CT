# 2016.11.19 19:51:30 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/QuestRecruitWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class QuestRecruitWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def onApply(self, data):
        self._printOverrideError('onApply')

    def as_setInitDataS(self, data):
        """
        :param data: Represented by TankmanCardVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\QuestRecruitWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:30 Støední Evropa (bìžný èas)
