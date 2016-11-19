# 2016.11.19 19:51:16 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanProfilePersonnelViewMeta.py
from gui.Scaleform.daapi.view.lobby.clans.profile.ClanProfileBaseView import ClanProfileBaseView

class ClanProfilePersonnelViewMeta(ClanProfileBaseView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends ClanProfileBaseView
    """

    def as_getMembersDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getMembersDP()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\ClanProfilePersonnelViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:16 Støední Evropa (bìžný èas)
