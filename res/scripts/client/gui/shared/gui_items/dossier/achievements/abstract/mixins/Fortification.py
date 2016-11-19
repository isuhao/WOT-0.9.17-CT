# 2016.11.19 19:52:55 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/gui/shared/gui_items/dossier/achievements/abstract/mixins/Fortification.py
from gui.shared.gui_items.dossier.achievements import validators

class Fortification(object):

    @classmethod
    def checkIsValid(cls, block, name, dossier):
        return validators.requiresFortification()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\shared\gui_items\dossier\achievements\abstract\mixins\Fortification.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:52:55 Støední Evropa (bìžný èas)
