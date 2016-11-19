# 2016.11.19 19:59:54 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_imports2.py
"""Fix incompatible imports and module references that must be fixed after
fix_imports."""
from . import fix_imports
MAPPING = {'whichdb': 'dbm',
 'anydbm': 'dbm'}

class FixImports2(fix_imports.FixImports):
    run_order = 7
    mapping = MAPPING
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\Lib\lib2to3\fixes\fix_imports2.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:59:55 Støední Evropa (bìžný èas)
