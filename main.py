import pyautogui
from constants import EMULATOR_REGION

s = pyautogui.screenshot(region=EMULATOR_REGION)
s.save('test.png')
