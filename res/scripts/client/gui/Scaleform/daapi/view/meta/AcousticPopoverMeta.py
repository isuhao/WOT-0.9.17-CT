# 2016.11.19 19:51:11 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/AcousticPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class AcousticPopoverMeta(SmartPopOverView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends SmartPopOverView
    """

    def onActionStart(self, actionID):
        self._printOverrideError('onActionStart')

    def onSpeakerClick(self, speakerID):
        self._printOverrideError('onSpeakerClick')

    def as_setDataS(self, data):
        """
        :param data: Represented by AcousticPopoverVo (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_onItemPlayS(self, itemsID):
        if self._isDAAPIInited():
            return self.flashObject.as_onItemPlay(itemsID)

    def as_onItemSelectS(self, itemsID):
        if self._isDAAPIInited():
            return self.flashObject.as_onItemSelect(itemsID)

    def as_setEnableS(self, isEnable):
        if self._isDAAPIInited():
            return self.flashObject.as_setEnable(isEnable)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\AcousticPopoverMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:11 Støední Evropa (bìžný èas)
