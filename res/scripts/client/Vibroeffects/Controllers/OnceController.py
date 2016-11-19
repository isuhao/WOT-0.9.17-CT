# 2016.11.19 19:54:57 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/Vibroeffects/Controllers/OnceController.py
import BigWorld
from Vibroeffects import VibroManager
from debug_utils import *

class OnceController:

    def __init__(self, effectName, gain = 100):
        VibroManager.g_instance.launchQuickEffect(effectName, 1, gain)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\Vibroeffects\Controllers\OnceController.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:54:57 Støední Evropa (bìžný èas)
