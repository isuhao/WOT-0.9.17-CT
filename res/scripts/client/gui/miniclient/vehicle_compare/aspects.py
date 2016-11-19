# 2016.11.19 19:48:50 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/miniclient/vehicle_compare/aspects.py
from helpers import aop

class MakeVehicleCompareUnavailable(aop.Aspect):

    def atReturn(self, cd):
        cd.change()
        return False
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\miniclient\vehicle_compare\aspects.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:48:50 Støední Evropa (bìžný èas)
