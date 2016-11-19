# 2016.11.19 19:49:05 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/prb_control/entities/event/squad/actions_handler.py
from CurrentVehicle import g_currentVehicle
from gui.prb_control.entities.base.squad.actions_handler import SquadActionsHandler
from helpers import dependency
from skeletons.gui.server_events import IEventsCache

class EventBattleSquadActionsHandler(SquadActionsHandler):
    """
    Event battle squad actions handler
    """
    eventsCache = dependency.descriptor(IEventsCache)

    def _loadWindow(self, ctx):
        super(EventBattleSquadActionsHandler, self)._loadWindow(ctx)
        if not self._entity.getPlayerInfo().isReady:
            eventVehicle = self.eventsCache.getEventVehicles()[0]
            g_currentVehicle.selectVehicle(eventVehicle.invID)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\prb_control\entities\event\squad\actions_handler.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:49:05 Støední Evropa (bìžný èas)
