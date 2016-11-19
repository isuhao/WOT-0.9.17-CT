# 2016.11.19 19:49:44 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/stats_exchage/__init__.py
import weakref
from gui.Scaleform.daapi.view.battle.shared.stats_exchage import broker
from gui.Scaleform.daapi.view.battle.shared.stats_exchage import player
from gui.Scaleform.daapi.view.battle.shared.stats_exchage.stats_ctrl import BattleStatisticsDataController
__all__ = ('BattleStatisticsDataController', 'createExchangeBroker')

def createExchangeBroker(exchangeCtx):
    proxy = weakref.proxy(exchangeCtx)
    exchangeBroker = broker.ExchangeBroker(exchangeCtx)
    exchangeBroker.setPlayerStatusExchange(player.PlayerStatusComponent())
    exchangeBroker.setUsersTagsExchange(player.UsersTagsListExchangeData(proxy))
    exchangeBroker.setInvitationsExchange(player.InvitationsExchangeBlock())
    return exchangeBroker
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\battle\shared\stats_exchage\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:49:44 Støední Evropa (bìžný èas)
