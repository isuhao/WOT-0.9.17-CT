# 2016.11.19 19:48:02 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/client/gui/InputHandler.py
import Event
g_instance = None

class _InputHandler:
    onKeyDown = Event.Event()
    onKeyUp = Event.Event()

    def handleKeyEvent(self, event):
        if event.isKeyDown():
            self.onKeyDown(event)
        else:
            self.onKeyUp(event)


g_instance = _InputHandler()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\scripts\client\gui\InputHandler.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2016.11.19 19:48:02 St�edn� Evropa (b�n� �as)