# 2016.11.19 19:52:51 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/PrematureDetonationAchievement.py
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as _AB
from abstract import SimpleProgressAchievement

class PrematureDetonationAchievement(SimpleProgressAchievement):

    def __init__(self, dossier, value = None):
        super(PrematureDetonationAchievement, self).__init__('prematureDetonationMedal', _AB.TEAM_7X7, dossier, value)

    def _readProgressValue(self, dossier):
        return dossier.getRecordValue(_AB.TEAM_7X7, 'prematureDetonation')
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\dossier\achievements\PrematureDetonationAchievement.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:52:51 St�edn� Evropa (b�n� �as)
