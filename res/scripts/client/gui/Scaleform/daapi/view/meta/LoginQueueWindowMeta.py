# 2016.11.19 19:51:27 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/LoginQueueWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class LoginQueueWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def onCancelClick(self):
        self._printOverrideError('onCancelClick')

    def onAutoLoginClick(self):
        self._printOverrideError('onAutoLoginClick')

    def as_setTitleS(self, title):
        if self._isDAAPIInited():
            return self.flashObject.as_setTitle(title)

    def as_setMessageS(self, message):
        if self._isDAAPIInited():
            return self.flashObject.as_setMessage(message)

    def as_setCancelLabelS(self, cancelLabel):
        if self._isDAAPIInited():
            return self.flashObject.as_setCancelLabel(cancelLabel)

    def as_showAutoLoginBtnS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_showAutoLoginBtn(value)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\LoginQueueWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:27 St�edn� Evropa (b�n� �as)
