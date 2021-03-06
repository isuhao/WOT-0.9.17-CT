# 2016.11.19 19:55:38 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/dossiers2/custom/club_layout.py
from dossiers2.common.DossierBlockBuilders import *
from battle_statistics_layouts import *
from dossiers2.custom.dependencies import CLUB_BATTLES_STAT_DEPENDENCIES
from dossiers2.custom.dependencies import CLUB_ACHIEVEMENTS_DEPENDENCIES
_rated7x7BlockBuilder = StaticSizeBlockBuilder('rated7x7', RATED_7X7_BLOCK_LAYOUT, {}, [])
_maxRated7x7BlockBuilder = StaticSizeBlockBuilder('maxRated7x7', MAX_AND_BEST_VEHICLE_BLOCK_LAYOUT, {}, [])
rated7x7DossierLayout = (_rated7x7BlockBuilder, _maxRated7x7BlockBuilder)
_clubTotalBlockLayout = ['creationTime', 'lastBattleTime']
_clubTotalBlockBuilder = StaticSizeBlockBuilder('total', _clubTotalBlockLayout, {}, [])
_clubBattlesBlockLayout = ['battlesCount',
 'wins',
 'losses',
 'killedVehicles',
 'lostVehicles',
 'capturePoints',
 'droppedCapturePoints',
 'damageDealt',
 'damageReceived',
 'battlesCountInAttack',
 'damageDealtInAttack',
 'damageDealtInDefence']
_clubBattlesBlockBuilder = StaticSizeBlockBuilder('clubBattles', _clubBattlesBlockLayout, CLUB_BATTLES_STAT_DEPENDENCIES, [])
_clubBestVehiclesBlockBuilder = DictBlockBuilder('vehicles', 'I', 'II', {})
_clubBestMapsBlockBuilder = DictBlockBuilder('maps', 'I', 'II', {})
CLUB_ACHIEVEMENTS_BLOCK_LAYOUT = ['tacticalAdvantage',
 'tacticalSkill',
 'secretOperations',
 'victoryMarchSeries',
 'maxVictoryMarchSeries',
 'strategicOperations']
_clubAchievementsPopUps = ['strategicOperations']
_clubAchievementsBlockBuilder = StaticSizeBlockBuilder('achievementsRated7x7', CLUB_ACHIEVEMENTS_BLOCK_LAYOUT, CLUB_ACHIEVEMENTS_DEPENDENCIES, _clubAchievementsPopUps)
_SINGLE_ACHIEVEMENTS_VALUES = ['victoryMarch']
_singleAchievementsPopUps = ['victoryMarch']
_singleAchievementsBlockBuilder = BinarySetDossierBlockBuilder('singleAchievementsRated7x7', _SINGLE_ACHIEVEMENTS_VALUES, {}, _singleAchievementsPopUps)
clubDossierLayout = (_clubTotalBlockBuilder,
 _clubBattlesBlockBuilder,
 _clubBestVehiclesBlockBuilder,
 _clubBestMapsBlockBuilder,
 _clubAchievementsBlockBuilder,
 _singleAchievementsBlockBuilder)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\dossiers2\custom\club_layout.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:55:38 St�edn� Evropa (b�n� �as)
