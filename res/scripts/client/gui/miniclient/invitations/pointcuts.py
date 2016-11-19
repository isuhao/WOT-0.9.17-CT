# 2016.11.19 19:48:47 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/miniclient/invitations/pointcuts.py
from helpers import aop
import aspects

class PrbDisableAcceptButton(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.prb_control.invites', 'InvitesManager', 'canAcceptInvite', aspects=(aspects.DisableAccept,))


class PrbInvitationText(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.prb_control.formatters.invites', 'PrbInviteHtmlTextFormatter', 'getNote', aspects=(aspects.InvitationNote,))


class ClubDisableAcceptButton(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'notification.decorators', 'ClubInviteDecorator', 'getListVO', aspects=(aspects.DisableAcceptButton,))


class ClubInvitationText(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.clubs.formatters', 'ClubInviteHtmlTextFormatter', 'getNote', aspects=(aspects.ClubInvitationNote,))


class ClubInvitationComment(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.clubs.formatters', 'ClubInviteHtmlTextFormatter', 'getComment', aspects=(aspects.ClubInvitationComment,))
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\miniclient\invitations\pointcuts.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:48:47 Støední Evropa (bìžný èas)
