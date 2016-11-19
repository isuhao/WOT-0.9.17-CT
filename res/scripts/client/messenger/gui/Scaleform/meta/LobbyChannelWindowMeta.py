# 2016.11.19 19:53:54 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/LobbyChannelWindowMeta.py
from messenger.gui.Scaleform.view.lobby.SimpleChannelWindow import SimpleChannelWindow

class LobbyChannelWindowMeta(SimpleChannelWindow):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SimpleChannelWindow
    """

    def as_getMembersDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getMembersDP()

    def as_hideMembersListS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideMembersList()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\messenger\gui\Scaleform\meta\LobbyChannelWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:53:54 Støední Evropa (bìžný èas)
