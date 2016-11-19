# 2016.11.19 19:48:55 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/prb_control/entities/base/listener.py
from gui.prb_control import prbDispatcherProperty, prbEntityProperty

class IPrbListener(object):
    """
    Base prebattle listener class.
    """

    @prbDispatcherProperty
    def prbDispatcher(self):
        return None

    @prbEntityProperty
    def prbEntity(self):
        return None

    def startPrbListening(self):
        """
        Start prebattle events listening.
        """
        self.prbEntity.addListener(self)

    def stopPrbListening(self):
        """
        Stop prebattle events listening.
        """
        if self.prbEntity is not None:
            self.prbEntity.removeListener(self)
        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\prb_control\entities\base\listener.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:48:55 Støední Evropa (bìžný èas)
