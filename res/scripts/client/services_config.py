# 2016.11.19 19:47:10 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/services_config.py
import account_helpers
import gui
__all__ = ('getClientServicesConfig',)

def getClientServicesConfig(manager):
    """ Configures services for package gui.
    :param manager: helpers.dependency.DependencyManager
    """
    manager.install(gui.getGuiServicesConfig)
    manager.install(account_helpers.getAccountHelpersConfig)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\services_config.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:47:10 Støední Evropa (bìžný èas)
