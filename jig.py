import pyautogui, sys
import time

mousepos = None
time_last = time.time()

try:
    while True:
        if (pyautogui.position() == mousepos): # no need for jig if mouse has moved
            pyautogui.press("volumemute")
            pyautogui.press("volumemute")
            print("[{:.2f}] Jigged".format(time.time()))
            
        mousepos = pyautogui.position()
        time.sleep(240)  # 1 jig per 4 sec

except KeyboardInterrupt:
    print('interrupted!')

