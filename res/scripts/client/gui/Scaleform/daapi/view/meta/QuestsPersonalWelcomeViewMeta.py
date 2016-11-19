# 2016.11.19 19:51:30 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/QuestsPersonalWelcomeViewMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class QuestsPersonalWelcomeViewMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def success(self):
        self._printOverrideError('success')

    def as_setDataS(self, data):
        """
        :param data: Represented by QuestsPersonalWelcomeViewVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)

    def as_showMiniClientInfoS(self, description, hyperlink):
        if self._isDAAPIInited():
            return self.flashObject.as_showMiniClientInfo(description, hyperlink)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\QuestsPersonalWelcomeViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:30 Støední Evropa (bìžný èas)
