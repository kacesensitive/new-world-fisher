import time
import pyautogui
from asyncio.tasks import sleep
starttime = time.time()
x = 0
while True:
    startButton = pyautogui.locateOnScreen('Capture.png', confidence = 0.7)
    if startButton == None:
        print("no fish waiting")
    if startButton != None:
        print("FISH!!!!!!!!!!!!")
        pyautogui.click()
        while True:
            meter = pyautogui.locateOnScreen('meter.png', confidence = 0.7)
            if meter == None:
                print("Hold Reeling In")
                x = x + 1
                if x > 20:
                    print("Fish caught!! Recasting!!")
                    pyautogui.mouseDown()
                    time.sleep(1.9)
                    pyautogui.mouseUp()
                    x = 0
                    break
            if meter != None:
                print("REEEEEEEL!!!!")
                x = 0
                pyautogui.mouseDown()
                time.sleep(1)
                pyautogui.mouseUp()
            time.sleep(0.01 - ((time.time() - starttime) % 0.01))
    time.sleep(0.01 - ((time.time() - starttime) % 0.01))