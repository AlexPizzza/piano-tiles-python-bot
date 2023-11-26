import time
import keyboard

import d3dshot

from constants import EMULATOR_REGION, LANES

d = d3dshot.create(capture_output='numpy')

print('Starting in 3...')
time.sleep(3)
while True:
    start_time = time.time()
    img = d.screenshot(region=EMULATOR_REGION)

    for lane in LANES:
        value = sum(img[lane['location']])
        if value < 50 or img[lane['location']][0] == 0:
            keyboard.press(lane['key'])
            time.sleep(.1)
        else:
            keyboard.release(lane['key'])

    if keyboard.is_pressed('q'):
        break
