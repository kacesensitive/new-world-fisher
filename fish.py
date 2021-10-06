import time
import pyautogui
from asyncio.tasks import sleep
starttime = time.time()
x = 0
y = 0
while True:
    startButton = pyautogui.locateOnScreen('Capture.png', confidence = 0.7)
    if startButton == None:
        y = y + 1
        if y > 200:
            print("something is fishy.... recasting")
            pyautogui.mouseDown()
            time.sleep(1.9)
            pyautogui.mouseUp()
            y = 0
        print("no fish waiting ", 200 - y)
    if startButton != None:
        print("FISH!!!!!!!!!!!!")
        y = 0
        pyautogui.click()
        while True:
            meter = pyautogui.locateOnScreen('meter.png', confidence = 0.7)
            if meter == None:
                print("Hold Reeling In")
                x = x + 1
                if x > 35:
                    fishingpole_durability = pyautogui.locateOnScreen('rod.png', confidence = 0.5)
                    if fishingpole_durability == None:
                        print("Pole broken: Attempting repair")
                        # tab for inventory
                        pyautogui.press('tab')
                        time.sleep(2)
                        print("Opened Inventory")
                        # locate broken rod
                        while True:
                            broken_rod = pyautogui.locateOnScreen('broken_rod.png', confidence = 0.7)
                            print ("checking for broken rod...")
                            if broken_rod != None:
                                print ("broken rod found")
                                time.sleep(2)
                                pyautogui.moveTo(broken_rod)
                                time.sleep(1)
                                pyautogui.click()
                                time.sleep(5)
                                break
                        while True:
                            repair_button = pyautogui.locateOnScreen('repair-button.png', confidence = 0.7)
                            print ("checking for repair button..")
                            if repair_button != None:
                                print ("button found")
                                break
                        time.sleep(3)
                        pyautogui.moveTo(repair_button)
                        time.sleep(1)
                        pyautogui.click()
                        print("Clicked broken rod for repair")
                        time.sleep(2)
                        while True:
                            confirm = pyautogui.locateOnScreen('confirm.png', confidence = 0.7)
                            print ("checking for confirm button")
                            if confirm != None:
                                time.sleep(1)
                                print("confirm found")
                                pyautogui.moveTo(confirm)
                                time.sleep(2)
                                pyautogui.click()
                                break
                        # click confirm
                        time.sleep(1)
                        time.sleep(1)
                        # tab to exit inventory
                        pyautogui.press('tab')
                        time.sleep(1)
                        print("Pole fixed: Recasting")
                        time.sleep(1)
                        pyautogui.press('f3')
                        time.sleep(1)
                        pyautogui.mouseDown()
                        time.sleep(1.9)
                        pyautogui.mouseUp()
                        x = 0
                        break
                    if fishingpole_durability != None:
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