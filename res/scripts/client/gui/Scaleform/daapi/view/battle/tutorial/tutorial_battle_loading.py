# 2016.11.19 19:49:44 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/tutorial/tutorial_battle_loading.py
from gui.Scaleform.daapi.view.battle.shared.battle_loading import BattleLoading
from gui.Scaleform.daapi.view.meta.TutorialLoadingMeta import TutorialLoadingMeta

class TutorialBattleLoading(BattleLoading, TutorialLoadingMeta):

    def invalidateArenaInfo(self):
        super(TutorialBattleLoading, self).invalidateArenaInfo()
        arenaInfoData = {'mapName': self._battleCtx.getArenaTypeName(),
         'battleTypeLocaleStr': self._battleCtx.getArenaDescriptionString(isInBattle=False),
         'battleTypeFrameLabel': self._battleCtx.getArenaFrameLabel()}
        self.as_setTutorialArenaInfoS(arenaInfoData)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\battle\tutorial\tutorial_battle_loading.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:49:44 Støední Evropa (bìžný èas)
