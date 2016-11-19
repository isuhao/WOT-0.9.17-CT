# 2016.11.19 19:48:50 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/miniclient/vehicle_compare/pointcuts.py
import aspects
from helpers import aop

class MakeVehicleCompareUnavailable(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.game_control.veh_comparison_basket', 'VehComparisonBasket', 'isAvailable', aspects=(aspects.MakeVehicleCompareUnavailable,))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\miniclient\vehicle_compare\pointcuts.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:48:50 Støední Evropa (bìžný èas)
