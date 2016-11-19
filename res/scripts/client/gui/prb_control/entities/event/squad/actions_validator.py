# 2016.11.19 19:49:05 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/prb_control/entities/event/squad/actions_validator.py
from gui.prb_control.entities.base.squad.actions_validator import SquadActionsValidator
from gui.prb_control.entities.base.unit.actions_validator import UnitVehiclesValidator

class EventBattleVehiclesValidator(UnitVehiclesValidator):
    """
    Event battle squad vehicles validation
    """

    def _isValidMode(self, vehicle):
        return vehicle.isEvent


class EventBattleSquadActionsValidator(SquadActionsValidator):
    """
    Event battle squad actions validation class
    """

    def _createVehiclesValidator(self, entity):
        return EventBattleVehiclesValidator(entity)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\prb_control\entities\event\squad\actions_validator.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:49:05 Støední Evropa (bìžný èas)
