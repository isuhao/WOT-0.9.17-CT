# 2016.11.19 19:48:03 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/SystemMessages.py
from enumerations import Enumeration
from gui.shared.money import Currency
from helpers import dependency
from skeletons.gui.system_messages import ISystemMessages
SM_TYPE = Enumeration('System message type', ['Error',
 'Warning',
 'Information',
 'GameGreeting',
 'PowerLevel',
 'FinancialTransactionWithGold',
 'FinancialTransactionWithCredits',
 'FortificationStartUp',
 'PurchaseForGold',
 'DismantlingForGold',
 'PurchaseForCredits',
 'Selling',
 'Remove',
 'Repair',
 'CustomizationForGold',
 'CustomizationForCredits',
 'Restore'])
CURRENCY_TO_SM_TYPE = {Currency.CREDITS: SM_TYPE.PurchaseForCredits,
 Currency.GOLD: SM_TYPE.PurchaseForGold}

def _getSystemMessages():
    return dependency.instance(ISystemMessages)


def pushMessage(text, type = SM_TYPE.Information, priority = None):
    _getSystemMessages().pushMessage(text, type, priority)


def pushI18nMessage(key, *args, **kwargs):
    _getSystemMessages().pushI18nMessage(key, *args, **kwargs)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\SystemMessages.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:48:03 St�edn� Evropa (b�n� �as)
