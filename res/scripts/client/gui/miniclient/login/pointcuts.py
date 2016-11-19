# 2016.11.19 19:48:49 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/miniclient/login/pointcuts.py
import aspects
from helpers import aop

class ShowBGWallpaper(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.login.LoginView', 'BackgroundMode', 'show$', aspects=(aspects.ShowBGWallpaper,))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\miniclient\login\pointcuts.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:48:49 Støední Evropa (bìžný èas)
