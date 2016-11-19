# 2016.11.19 19:49:04 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/prb_control/entities/company/legacy/limits.py
from gui.prb_control.entities.base.limits import LimitsCollection, VehicleIsValid, VehiclesLevelLimit, TeamIsValid

class CompanyLimits(LimitsCollection):
    """
    Company limits class
    """

    def __init__(self, entity):
        super(CompanyLimits, self).__init__(entity, (VehicleIsValid(),), (VehiclesLevelLimit(), TeamIsValid()))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\prb_control\entities\company\legacy\limits.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:49:04 Støední Evropa (bìžný èas)
