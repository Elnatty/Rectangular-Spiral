import pyautogui
import time
time.sleep(2)

# print(pyautogui.size())
# print(pyautogui.position())
# pyautogui.moveTo(1343,16,2)
# pyautogui.moveRel(200,100,3)
# pyautogui.click(789,227,3,3)
# pyautogui.scroll(-1000)

# This automatically draws a rectangular spiral.
distance = 200
pyautogui.moveTo(386, 336, 1)
while distance > 0:
    pyautogui.dragRel(distance, 0, 1, button='left')
    distance -= 20
    pyautogui.dragRel(0, distance, 1, button='left')
    pyautogui.dragRel(-distance, 0, 1, button='left')
    distance -= 20
    pyautogui.dragRel(0, -distance, 1, button='left')
    pyautogui.typewrite()

# Note>> everything is based on my PC's screen resolution..