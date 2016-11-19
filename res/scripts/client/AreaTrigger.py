# 2016.11.19 19:46:50 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/AreaTrigger.py
import BigWorld
import TriggersManager

class AreaTrigger(BigWorld.UserDataObject):

    def __init__(self):
        BigWorld.UserDataObject.__init__(self)
        self.__id = TriggersManager.g_manager.addTrigger(TriggersManager.TRIGGER_TYPE.AREA, name=self.name, position=self.position, radius=self.radius, exitInterval=self.exitInterval)

    def destroy(self):
        TriggersManager.g_manager.delTrigger(self.__id)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\AreaTrigger.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:46:50 Støední Evropa (bìžný èas)
