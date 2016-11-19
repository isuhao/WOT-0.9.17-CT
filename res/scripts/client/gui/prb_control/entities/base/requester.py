# 2016.11.19 19:48:55 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/prb_control/entities/base/requester.py


class IPrbListRequester(object):
    """
    Interface for prebattles list request.
    """

    def start(self, callback):
        """
        Starts to listen required events.
        Args:
            callback: routine that is invoked when list will be received/updated
        """
        pass

    def stop(self):
        """
        Stop to listen required events.
        """
        pass

    def request(self, ctx = None):
        """
        Send request to update list.
        Args:
            ctx: request context
        """
        pass
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\prb_control\entities\base\requester.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:48:55 Støední Evropa (bìžný èas)
