import time
import random
import pyautogui
from asyncio.tasks import sleep

BAIT = 'bait.png'
METER = 'meter.png'
ROD = 'rod.png'
BROKEN_ROD = 'broken_rod.png'
REPAIR_BUTTON = 'repair-button.png'
CONFIRM_BUTTON = 'confirm.png'

KEY_CAMERA = 'B'
KEY_INVENTORY = 'TAB'
KEY_FISHING = 'F3'

THROW_MAX_FLAG = True

def randomTime(starttime = 0.5, endtime = 1.5):
    return round(random.uniform(starttime, endtime), 2)


def reelRod():
    print("REEEEEEEL!!!!")
    pyautogui.mouseDown()
    time.sleep(randomTime (0.7, 1))
    pyautogui.mouseUp()


def throwingRod():
    global THROW_MAX_FLAG
    pyautogui.mouseDown()
    if THROW_MAX_FLAG:
        time.sleep(1.91)
        THROW_MAX_FLAG = False
    else:
        time.sleep(randomTime(1, 1.91))
        THROW_MAX_FLAG = True
    pyautogui.mouseUp()


def fishCaught():
    print("Fish caught!! Recasting!!")
    pyautogui.keyUp(KEY_CAMERA)
    pyautogui.keyDown(KEY_CAMERA)
    time.sleep(0.5)
    throwingRod()


def locateIcon(name, confidence = 0.7):
    return pyautogui.locateOnScreen(name, confidence = confidence)


def repairRod():
    print("Pole broken: Attempting repair")
    # Opening inventory
    pyautogui.press(KEY_INVENTORY)
    time.sleep(2)
    print("Opened Inventory")

    # Locating broken rod
    while True:
        broken_rod = locateIcon(BROKEN_ROD)
        print ("Checking for broken rod...")
        if broken_rod != None:
            print ("Broken rod found")
            time.sleep(2)
            pyautogui.moveTo(broken_rod)
            time.sleep(1)
            pyautogui.click()
            time.sleep(5)
            break

    ## Managing repair button
    while True:
        repair_button = locateIcon(REPAIR_BUTTON, 0.5)
        print ("Expecting for repair button...")
        if repair_button != None:
            print ("Repair button found")
            time.sleep(3)
            pyautogui.moveTo(repair_button)
            time.sleep(1)
            pyautogui.click()
            print("Repair button has been clicked")
            break
        time.sleep(0.3)

    
    ## Managing confirm button
    time.sleep(2)
    while True:
        confirm = locateIcon(CONFIRM_BUTTON)
        print ("Expecting for confirm button")
        if confirm != None:
            time.sleep(1)
            print("Confirm button found")
            pyautogui.moveTo(confirm)
            time.sleep(2)
            pyautogui.click()
            print("Confirm button has been clicked")
            break

    ## Waiting to close inventory...
    time.sleep(2)
    pyautogui.press(KEY_INVENTORY)
    time.sleep(1)
    print("Pole fixed: Recasting")

    ## Recasting!
    time.sleep(1)
    pyautogui.press(KEY_FISHING)
    time.sleep(1)
    throwingRod()


def takeBaitProcess(starttime):
    checkingRod = 0
    limit = 26 + random.randrange(10)
    while True:
        meterIcon = locateIcon(METER)
        pyautogui.keyDown(KEY_CAMERA)
        
        ## Meter icon does not match, keep calm!
        if meterIcon == None:
            print("Hold Reeling In")
            
            ### Checking status fishing rod
            if checkingRod > limit:
                fishingpole_durability = locateIcon(ROD, confidence = 0.6)

                if fishingpole_durability == None:
                    repairRod()
                    break

                if fishingpole_durability != None:
                    fishCaught()
                    checkingRod = 0
                    break

            checkingRod += 1

        ## If meter is found, reel!
        if meterIcon != None:
            reelRod()
            ### Rod seems good, reseting counter
            checkingRod = 0
        time.sleep(0.01 - ((time.time() - starttime) % 0.01))


def main():
    # Sleep before fishing
    time.sleep(3)

    starttime = time.time()
    pyautogui.keyDown(KEY_CAMERA)
    throwingRod()
    retryCasting = 0
    while True:
        # Blocking camera before start
        pyautogui.keyDown(KEY_CAMERA)

        # Checking icon capture to start the main process
        baitIcon = pyautogui.locateOnScreen(BAIT, confidence = 0.7, grayscale = True)
        if baitIcon == None:
            retryCasting += 1
            if retryCasting > 200:
                print("Something is fishy.... recasting")
                throwingRod()
                retryCasting = 0
            print("no fish waiting ", 200 - retryCasting)

        if baitIcon != None:
            # When capture icon appears on the screen, click to start holding process
            pyautogui.click()
            print("FISH!!!!!!!!!!!!")
            retryCasting = 0
            takeBaitProcess(starttime)
            
        time.sleep(0.01 - ((time.time() - starttime) % 0.01))


if __name__ == "__main__":
    main()