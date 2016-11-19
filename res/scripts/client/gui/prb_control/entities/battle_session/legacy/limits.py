# 2016.11.19 19:49:03 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/prb_control/entities/battle_session/legacy/limits.py
from gui.prb_control.entities.base.limits import LimitsCollection, VehicleIsValid, VehiclesLevelLimit, TeamIsValid

class BattleSessionLimits(LimitsCollection):
    """
    Battle session limits class
    """

    def __init__(self, entity):
        super(BattleSessionLimits, self).__init__(entity, (VehicleIsValid(),), (VehiclesLevelLimit(), TeamIsValid()))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\prb_control\entities\battle_session\legacy\limits.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:49:03 Støední Evropa (bìžný èas)
