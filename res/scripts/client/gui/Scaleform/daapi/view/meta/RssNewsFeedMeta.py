# 2016.11.19 19:51:32 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/RssNewsFeedMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RssNewsFeedMeta(BaseDAAPIComponent):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends BaseDAAPIComponent
    """

    def openBrowser(self, linkToOpen):
        self._printOverrideError('openBrowser')

    def as_updateFeedS(self, feed):
        """
        :param feed: Represented by Vector.<RssItemVo> (AS)
        """
        if self._isDAAPIInited():
            return self.flashObject.as_updateFeed(feed)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\Scaleform\daapi\view\meta\RssNewsFeedMeta.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:51:32 Støední Evropa (bìžný èas)
