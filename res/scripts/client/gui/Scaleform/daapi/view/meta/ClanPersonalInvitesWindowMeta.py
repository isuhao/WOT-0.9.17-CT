# 2016.11.19 19:51:15 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanPersonalInvitesWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ClanPersonalInvitesWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def as_setActualInvitesTextS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setActualInvitesText(value)

    def as_showWaitingAnimationS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showWaitingAnimation(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\ClanPersonalInvitesWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:15 Støední Evropa (bìžný èas)
