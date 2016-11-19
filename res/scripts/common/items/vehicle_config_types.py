# 2016.11.19 19:56:02 Støední Evropa (bìžný èas)
# Embedded file name: scripts/common/items/vehicle_config_types.py
from collections import namedtuple
LodSettings = namedtuple('LodSettings', ['maxLodDistance', 'maxPriority'])
LeveredSuspensionConfig = namedtuple('LeveredSuspensionConfig', ['levers', 'interpolationSpeedMul', 'lodSettings'])
SuspensionLever = namedtuple('SuspensionLever', ['startNodeName',
 'jointNodeName',
 'trackNodeName',
 'minAngle',
 'maxAngle'])
SoundSiegeModeStateChange = namedtuple('SoundSiegeModeStateChange', ['on', 'off'])
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\common\items\vehicle_config_types.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:56:02 Støední Evropa (bìžný èas)
