# 2016.11.19 19:51:26 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/LegalInfoWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class LegalInfoWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def getLegalInfo(self):
        self._printOverrideError('getLegalInfo')

    def onCancelClick(self):
        self._printOverrideError('onCancelClick')

    def as_setLegalInfoS(self, legalInfo):
        if self._isDAAPIInited():
            return self.flashObject.as_setLegalInfo(legalInfo)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\LegalInfoWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:26 Støední Evropa (bìžný èas)
