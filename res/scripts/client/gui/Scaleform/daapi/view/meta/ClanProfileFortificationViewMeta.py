# 2016.11.19 19:51:15 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ClanProfileFortificationViewMeta.py
from gui.Scaleform.daapi.view.lobby.clans.profile.ClanProfileBaseView import ClanProfileBaseView

class ClanProfileFortificationViewMeta(ClanProfileBaseView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends ClanProfileBaseView
    """

    def as_showBodyDummyS(self, data):
        """
        :param data: Represented by DummyVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_showBodyDummy(data)

    def as_hideBodyDummyS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideBodyDummy()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\ClanProfileFortificationViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:15 Støední Evropa (bìžný èas)
