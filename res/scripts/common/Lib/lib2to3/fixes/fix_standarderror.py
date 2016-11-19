# 2016.11.19 19:59:57 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_standarderror.py
"""Fixer for StandardError -> Exception."""
from .. import fixer_base
from ..fixer_util import Name

class FixStandarderror(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n              'StandardError'\n              "

    def transform(self, node, results):
        return Name(u'Exception', prefix=node.prefix)
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\Lib\lib2to3\fixes\fix_standarderror.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:59:57 Støední Evropa (bìžný èas)
