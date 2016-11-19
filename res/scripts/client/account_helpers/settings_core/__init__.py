# 2016.11.19 19:47:30 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/account_helpers/settings_core/__init__.py
from account_helpers.settings_core.SettingsCache import SettingsCache
from account_helpers.settings_core.SettingsCore import SettingsCore
from skeletons.account_helpers.settings_core import ISettingsCache, ISettingsCore

def getSettingsCoreConfig(manager):
    """ Configures services for package gui.
    :param manager: helpers.dependency.DependencyManager
    """
    cache = SettingsCache()
    manager.bindInstance(ISettingsCache, cache, finalizer='fini')
    core = SettingsCore()
    manager.bindInstance(ISettingsCore, core, finalizer='fini')
    cache.init()
    core.init()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\account_helpers\settings_core\__init__.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:47:30 Støední Evropa (bìžný èas)
