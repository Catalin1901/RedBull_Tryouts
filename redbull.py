import win32api, win32con
import time
from PIL import ImageGrab, Image
import mouse
import cv2 as cv
import numpy as np

def click(x,y): 
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def localizare(poza, method):
  img = ImageGrab.grab(bbox=(0, 100, 500, 210))
  img_cv = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
  res = cv.matchTemplate(img_cv, poza , method)
  # print(res)
  return (res >= 0.8).any()

def localizare_mare(poza, method):
  img = ImageGrab.grab(bbox=(0, 100, 710, 210))
  img_cv = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
  res = cv.matchTemplate(img_cv, poza , method)
  # print(res)
  return (res >= 0.85).any()

def buton(x, y):
  mouse.move(x,y)
  mouse.click('left')





time.sleep(2)

lent = cv.imread(r'Pictures\lent.png')
DRS = cv.imread(r'Pictures\drs.png')
lauda = cv.imread(r'Pictures\lauda.png')
mare = cv.imread(r'Pictures\mare.png')
mica = cv.imread(r'Pictures\mica.png')
radar = cv.imread(r'Pictures\radar.png')
rapid = cv.imread(r'Pictures\rapid.png')
tribuna = cv.imread(r'Pictures\Tribuna.png')
boxe = cv.imread(r'Pictures\boxe.png')


print("Start")
print("When task finished, close the window")

while True:
  if localizare(lent, cv.TM_CCOEFF_NORMED):
   buton("61", "397")

  if localizare(DRS, cv.TM_CCOEFF_NORMED):
   buton("423", "594")

  if localizare(lauda, cv.TM_CCOEFF_NORMED):
   buton("180", "658")

  if localizare_mare(mare, cv.TM_CCOEFF_NORMED):
   buton("92", "390")

  if localizare_mare(mica, cv.TM_CCOEFF_NORMED):
   buton("291", "655")

  if localizare(radar, cv.TM_CCOEFF_NORMED):
   buton("276", "445")

  if localizare(rapid, cv.TM_CCOEFF_NORMED):
   buton("112", "477")

  if localizare(tribuna, cv.TM_CCOEFF_NORMED):
   buton("138", "569")

  if localizare(boxe, cv.TM_CCOEFF_NORMED):
   buton("432", "617")


