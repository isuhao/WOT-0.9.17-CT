# 2016.11.19 19:51:35 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/TickerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class TickerMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def showBrowser(self, entryID):
        self._printOverrideError('showBrowser')

    def as_setItemsS(self, items):
        """
        :param items: Represented by Vector.<RSSEntryVO> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_setItems(items)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\TickerMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:35 Støední Evropa (bìžný èas)
