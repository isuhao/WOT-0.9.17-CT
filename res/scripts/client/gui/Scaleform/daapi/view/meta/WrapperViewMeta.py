# 2016.11.19 19:51:37 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/WrapperViewMeta.py
from gui.Scaleform.framework.entities.View import View

class WrapperViewMeta(View):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends View
    """

    def onWindowClose(self):
        self._printOverrideError('onWindowClose')

    def as_showWaitingS(self, msg, props):
        if self._isDAAPIInited():
            return self.flashObject.as_showWaiting(msg, props)

    def as_hideWaitingS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideWaiting()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\WrapperViewMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:37 Støední Evropa (bìžný èas)
