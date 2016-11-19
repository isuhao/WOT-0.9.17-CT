# 2016.11.19 19:48:54 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/prb_control/entities/listener.py
from gui.prb_control.entities.base.legacy.listener import ILegacyListener
from gui.prb_control.entities.base.listener import IPrbListener
from gui.prb_control.entities.base.pre_queue.listener import IPreQueueListener
from gui.prb_control.entities.base.unit.listener import IUnitListener

class IGlobalListener(ILegacyListener, IUnitListener, IPreQueueListener, IPrbListener):

    def onPrbEntitySwitching(self):
        pass

    def onPrbEntitySwitched(self):
        pass

    def startGlobalListening(self):
        if self.prbDispatcher:
            self.prbDispatcher.addListener(self)

    def stopGlobalListening(self):
        if self.prbDispatcher:
            self.prbDispatcher.removeListener(self)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\prb_control\entities\listener.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:48:54 Støední Evropa (bìžný èas)
