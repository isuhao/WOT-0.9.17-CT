# 2016.11.19 19:50:40 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/messengerBar/VehicleCompareCartButton.py
from gui.Scaleform.daapi.view.meta.ButtonWithCounterMeta import ButtonWithCounterMeta
from helpers import dependency
from skeletons.gui.game_control import IVehicleComparisonBasket

class VehicleCompareCartButton(ButtonWithCounterMeta):
    comparisonBasket = dependency.descriptor(IVehicleComparisonBasket)

    def __init__(self):
        super(VehicleCompareCartButton, self).__init__()

    def _populate(self):
        super(VehicleCompareCartButton, self)._populate()
        self.comparisonBasket.onChange += self.__onCountChanged
        self.comparisonBasket.onSwitchChange += self.destroy
        self.__changeCount(self.comparisonBasket.getVehiclesCount())

    def _dispose(self):
        self.comparisonBasket.onChange -= self.__onCountChanged
        self.comparisonBasket.onSwitchChange -= self.destroy
        super(VehicleCompareCartButton, self)._dispose()

    def __onCountChanged(self, _):
        """
        gui.game_control.VehComparisonBasket.onChange event handler
        :param _: instance of gui.game_control.veh_comparison_basket._ChangedData
        """
        self.__changeCount(self.comparisonBasket.getVehiclesCount())

    def __changeCount(self, count):
        self.as_setCountS(count)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\lobby\messengerBar\VehicleCompareCartButton.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:50:40 St�edn� Evropa (b�n� �as)