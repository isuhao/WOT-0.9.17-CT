# 2016.11.19 19:51:36 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/VehicleBuyWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class VehicleBuyWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    """

    def submit(self, data):
        self._printOverrideError('submit')

    def storeSettings(self, expanded):
        self._printOverrideError('storeSettings')

    def as_setGoldS(self, gold):
        if self._isDAAPIInited():
            return self.flashObject.as_setGold(gold)

    def as_setCreditsS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCredits(value)

    def as_setInitDataS(self, data):
        """
        :param data: Represented by BuyingVehicleVO (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_setEnabledSubmitBtnS(self, enabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setEnabledSubmitBtn(enabled)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\VehicleBuyWindowMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:36 St�edn� Evropa (b�n� �as)
