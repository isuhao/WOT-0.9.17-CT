# 2016.11.19 19:47:18 Støední Evropa (bìžný èas)
# Embedded file name: scripts/client/WWISE.py
enabled = True
try:
    from _WWISE import *
    import _WWISE
except ImportError:
    print 'WARNING: WWISE support is not enabled.'
    enabled = False
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\WWISE.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:47:18 Støední Evropa (bìžný èas)
