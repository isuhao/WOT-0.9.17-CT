# 2016.11.19 19:51:09 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/logitech/battle_loading.py
from gui.Scaleform import getPathForFlash, SCALEFORM_SWF_PATH
from gui.Scaleform.daapi.view.logitech.LogitechMonitorMeta import LogitechMonitorBattleLoadingColoredScreenMeta, LogitechMonitorMonoScreenMeta
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

def _getData():
    """
    :return: (arenaDescription, arenaTypeName, icon)
    """
    sessionProvider = dependency.descriptor(IBattleSessionProvider)
    if sessionProvider is not None:
        ctx = sessionProvider.getCtx()
        if ctx is not None:
            return (ctx.getArenaDescriptionString(), ctx.getArenaTypeName(), ctx.getArenaScreenIcon())
    return (None, None, None)


class LogitechMonitorBattleLoadingMonoScreen(LogitechMonitorMonoScreenMeta):

    def _onLoaded(self):
        arenaDescription, arenaTypeName, _ = _getData()
        text = '{}\r\n{}'.format(arenaTypeName, arenaDescription)
        self.as_setText(text)


class LogitechMonitorBattleLoadingColoredScreen(LogitechMonitorBattleLoadingColoredScreenMeta):

    def _onLoaded(self):
        arenaDescription, arenaTypeName, icon = _getData()
        icon = getPathForFlash(icon, base=SCALEFORM_SWF_PATH)
        self.as_setMap(arenaTypeName, arenaDescription, icon)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\logitech\battle_loading.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:09 Støední Evropa (bìžný èas)
