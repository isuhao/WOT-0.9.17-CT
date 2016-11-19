# 2016.11.19 19:53:54 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/ContactNoteManageViewMeta.py
from messenger.gui.Scaleform.meta.BaseManageContactViewMeta import BaseManageContactViewMeta

class ContactNoteManageViewMeta(BaseManageContactViewMeta):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseManageContactViewMeta
    """

    def sendData(self, data):
        self._printOverrideError('sendData')

    def as_setUserPropsS(self, value):
        """
        :param value: Represented by ContactUserPropVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setUserProps(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\messenger\gui\Scaleform\meta\ContactNoteManageViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:53:54 Støední Evropa (bìžný èas)
