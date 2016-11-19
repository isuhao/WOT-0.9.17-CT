# 2016.11.19 19:51:29 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ProfileSummaryWindowMeta.py
from gui.Scaleform.daapi.view.lobby.profile.ProfileSummary import ProfileSummary

class ProfileSummaryWindowMeta(ProfileSummary):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends ProfileSummary
    """

    def openClanStatistic(self):
        self._printOverrideError('openClanStatistic')

    def openClubProfile(self, clubDbID):
        self._printOverrideError('openClubProfile')

    def as_setClanDataS(self, data):
        """
        :param data: Represented by ProfileGroupBlockVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClanData(data)

    def as_setClubDataS(self, data):
        """
        :param data: Represented by ProfileGroupBlockVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setClubData(data)

    def as_setClanEmblemS(self, source):
        if self._isDAAPIInited():
            return self.flashObject.as_setClanEmblem(source)

    def as_setClubEmblemS(self, source):
        if self._isDAAPIInited():
            return self.flashObject.as_setClubEmblem(source)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\ProfileSummaryWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:29 Støední Evropa (bìžný èas)
