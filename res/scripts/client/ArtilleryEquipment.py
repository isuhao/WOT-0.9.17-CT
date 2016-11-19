# 2016.11.19 19:46:50 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/ArtilleryEquipment.py
from AvatarInputHandler import mathUtils
import BigWorld
from Math import Vector3

class ArtilleryEquipment(BigWorld.UserDataObject):

    def __init__(self):
        BigWorld.UserDataObject.__init__(self)
        launchDir = mathUtils.createRotationMatrix((self.__dict__['yaw'], self.__dict__['pitch'], 0)).applyToAxis(2)
        launchDir.normalise()
        self.launchVelocity = launchDir * self.speed
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\ArtilleryEquipment.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:46:50 St�edn� Evropa (b�n� �as)
