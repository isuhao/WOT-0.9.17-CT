# 2016.11.19 19:50:38 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/header/LobbyTicker.py
import BigWorld
from debug_utils import LOG_ERROR
from gui import GUI_SETTINGS
from gui.Scaleform.daapi.view.common.BaseTicker import BaseTicker
from helpers import dependency
from skeletons.gui.game_control import IBrowserController

class LobbyTicker(BaseTicker):
    browserCtrl = dependency.descriptor(IBrowserController)

    def __init__(self):
        super(LobbyTicker, self).__init__()

    def _handleBrowserLink(self, link):
        openBrowser = BigWorld.wg_openWebBrowser
        if GUI_SETTINGS.movingText.internalBrowser:
            browser = self.browserCtrl
            if browser is not None:
                openBrowser = browser.load
            else:
                LOG_ERROR('Attempting to open internal browser with page: `%s`,but browser is not exist. External browser will be opened.' % str(link))
        openBrowser(link)
        return
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\lobby\header\LobbyTicker.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:50:38 Støední Evropa (bìžný èas)
