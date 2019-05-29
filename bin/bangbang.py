'''Autoclicker to play the game bloody day http://www.bngames.com/games/bloody-day-1/full_screen.html.
Works best in full screen at 100% zoom in chrome.'''

import pyautogui

while True:

    # Bool to determine direction of target
    right = False
    left = False

    # Target detection logic
    im = pyautogui.screenshot(region=(200, 400, 800, 350))
    target = pyautogui.locate('assets/right.png', im, grayscale=False, confidence = 0.5)
    target2 = pyautogui.locate('assets/left.png', im, grayscale=False, confidence = 0.5)

    # Two if blocks are used to determine the direction the target is movement
    # Right moving target handler
    if target != None and left == False:
        right = True
    # In order to compensate for computational delay, numbers are added to the targets pixel position
        x_r = target[0]+200 
        y_r = target[1]+400
    # Firing loop
        for i in range(11):
            # Because of processing, overhead, and target speed the numbers added to x and y are fined tuned to current code.
            # Its reccomended these be left as are or changed and tuned again if the code is altered.
            pyautogui.click(x_r +185+(i*5), y_r+20)
        pyautogui.moveTo(736, 519)    
        right = False
    # Left moving target handler
    if target2 != None and right == False:
        left = True
        x_l = target2[0]+200
        y_l = target2[1]+400
        if target2[0] - 185 -50 > 0:
            for i in range(11):
                pyautogui.click(x_l-185-(i*5), y_l+20)
            pyautogui.moveTo(736, 519)
            left = False