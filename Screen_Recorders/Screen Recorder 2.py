import datetime
import time
import numpy as np
import cv2
import pyautogui
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

screen_size = (width,height)
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{time_stamp}.mkv'

fourcc = cv2.VideoWriter_fourcc(*"XVID")
#fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
out = cv2.VideoWriter(filename,fourcc,20,(screen_size))

fps = 102

prev = 0

while True:
    time_elapsed = time.time()-prev

    img = pyautogui.screenshot()

    if time_elapsed>1.0/fps:
        prev = time.time()
        frame = np.array(img)
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        cv2.imshow("addf", frame)
        out.write(frame)

    cv2.waitKey(100)
