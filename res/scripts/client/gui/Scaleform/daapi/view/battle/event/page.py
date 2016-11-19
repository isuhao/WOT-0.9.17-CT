# 2016.11.19 19:49:27 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/event/page.py
from gui.Scaleform.daapi.view.battle.classic.page import ClassicPage
from debug_utils import LOG_DEBUG

class EventBattlePage(ClassicPage):

    def _populate(self):
        super(EventBattlePage, self)._populate()
        LOG_DEBUG('Event battle page is created.')

    def _dispose(self):
        super(EventBattlePage, self)._dispose()
        LOG_DEBUG('Event battle page is destroyed.')
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\battle\event\page.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:49:27 Støední Evropa (bìžný èas)
