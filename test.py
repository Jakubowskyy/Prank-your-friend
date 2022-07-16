
import time
import webbrowser
from pynput.keyboard \
import Key,Controller
keyboard = Controller()

time.sleep(5)
webbrowser.open_new_tab('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
keyboard = Controller()
while True:
    for i in range(25):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        time.sleep(0.1)
    time.sleep(1)
    break
