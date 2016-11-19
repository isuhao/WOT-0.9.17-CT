# 2016.11.19 19:49:02 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/prb_control/entities/base/unit/scheduler.py
import weakref
from gui.shared.utils.scheduled_notifications import Notifiable

class UnitScheduler(Notifiable):
    """
    Class that process schedules for unit functionality
    """

    def __init__(self, entity):
        super(UnitScheduler, self).__init__()
        self._entity = weakref.proxy(entity)

    def init(self):
        """
        Initialization method
        """
        pass

    def fini(self):
        """
        Finalization method
        """
        pass
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\prb_control\entities\base\unit\scheduler.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:49:02 Støední Evropa (bìžný èas)
