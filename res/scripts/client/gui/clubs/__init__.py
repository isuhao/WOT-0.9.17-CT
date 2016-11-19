# 2016.11.19 19:48:32 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/clubs/__init__.py
from skeletons.gui.clubs import IClubsController
__all__ = ('getClubsServicesConfig',)

def getClubsServicesConfig(manager):
    """ Configures services for package clubs.
    :param manager: helpers.dependency.DependencyManager
    """
    from gui.clubs.ClubsController import ClubsController
    ctrl = ClubsController()
    ctrl.init()
    manager.bindInstance(IClubsController, ctrl, finalizer='fini')
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\clubs\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:48:32 Støední Evropa (bìžný èas)
