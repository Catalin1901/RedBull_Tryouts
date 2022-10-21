import win32api, win32con
import time
from PIL import ImageGrab, Image
import mouse
import cv2 as cv
import numpy as np

schimba = cv.imread(r'Pictures\schimba.png')
start_poza = cv.imread(r'Pictures\start.png')

def click(): 
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
  time.sleep(0.01) 
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def schimba_viteza(method):

  img = ImageGrab.grab(bbox=(130, 130, 275, 161))
  img_cv = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
  res = cv.matchTemplate(img_cv, schimba , method)
  return (res >= 0.7).any()

def start(method):
  img = ImageGrab.grab(bbox=(190, 125, 310, 170))
  img_cv = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
  res = cv.matchTemplate(img_cv, start_poza , method)
  # print(res)
  return (res >= 0.8).any()


time.sleep(2)




print("Start")

while True:
  if start(cv.TM_CCOEFF_NORMED) == True:
    mouse.click('left')
    break

while True:
  if schimba_viteza(cv.TM_CCOEFF_NORMED) == True:
    mouse.click('left')
    
  

