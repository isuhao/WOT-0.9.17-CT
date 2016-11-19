# 2016.11.19 19:47:54 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/FX/ClientCompatibility.py
import BigWorld
if BigWorld.component == 'editor':

    def addMat(a, b):
        return 0


    def delMat(a):
        return 0


    BigWorld.addMat = addMat
    BigWorld.delMat = delMat

    def player():
        return None


    BigWorld.player = player
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\FX\ClientCompatibility.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:47:54 Støední Evropa (bìžný èas)
