# 2016.11.19 19:47:04 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/GasAttack.py
import BigWorld
from debug_utils import LOG_DEBUG

class GasAttack(BigWorld.UserDataObject):

    def __init__(self):
        BigWorld.UserDataObject.__init__(self)
        LOG_DEBUG('GasAttack ', self.position)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\GasAttack.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:47:04 Støední Evropa (bìžný èas)
