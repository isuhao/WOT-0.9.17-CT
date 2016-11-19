# 2016.11.19 19:54:50 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/tutorial/gui/Scaleform/meta/TutorialBattleStatisticMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class TutorialBattleStatisticMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def restart(self):
        self._printOverrideError('restart')

    def showVideoDialog(self):
        self._printOverrideError('showVideoDialog')

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\tutorial\gui\Scaleform\meta\TutorialBattleStatisticMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:54:50 Støední Evropa (bìžný èas)
