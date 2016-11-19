# 2016.11.19 19:48:49 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/miniclient/lobby/profile/pointcuts.py
from helpers import aop
import aspects

class MakeClanBtnUnavailable(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.profile.ProfileSummaryWindow', 'ProfileSummaryWindow', '_getClanBtnParams', aspects=(aspects.MakeClanBtnUnavailable(),))


class MakeClubProfileButtonUnavailable(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.Scaleform.daapi.view.lobby.profile.ProfileSummaryWindow', 'ProfileSummaryWindow', '_getClubProfileButtonParams', aspects=(aspects.MakeClubProfileButtonUnavailable(),))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\miniclient\lobby\profile\pointcuts.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:48:49 St�edn� Evropa (b�n� �as)
