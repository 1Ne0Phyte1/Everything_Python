import time

import numpy
from ppadb.client import Client
from PIL import Image
import numpy as np

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()
# print(devices)
if len(devices) ==0:
    print('no device attached')
    quit()

# Selecting Device
device = devices[0]

while True:
    #Image capture

    image = device.screencap()
    with open('screen.png', 'wb') as f:
        f.write(image)

    image = Image.open('screen.png')
    image = numpy.array(image, dtype=numpy.uint8)

    pixels = [list(i[:3]) for i in image[2100]]

    transitions = []
    ignore =True
    black = True
    for i,pixel in enumerate(pixels):
        r,g,b = [int(i) for i in pixel]
        # print(r,g,b)
        if ignore and (r+g+b) !=0:
            continue

        ignore = False

        if black and (r+g+b) !=0:
            black = not black
            transitions.append(i)
            continue
        if not black and (r+g+b) == 0:
            black = not black
            transitions.append(i)
            continue

    # print(transitions)

    start, target1, target2 = transitions
    gap = target1-start
    target = target2- target1
    distance = (gap+target/2) * .98

    # print(distance)
    print(f'transition points : {transitions}, distance : {distance}')
    device.shell(f'input touchscreen swipe 500 500 500 500 {int(distance)}')
    time.sleep(2.3)
