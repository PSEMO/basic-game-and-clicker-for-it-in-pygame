import pyautogui
import win32api
import win32con
import keyboard
import time
from PIL import ImageGrab
from PIL import Image

def Click(position):
    #print(f"Clicking at position {position}")
    time.sleep(0.0001)
    win32api.SetCursorPos(position)
    time.sleep(0.0001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.0001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

x = 0
y = 0

while 1:
    time.sleep(0.0001)
    if keyboard.is_pressed('a'):
        x, y = pyautogui.position()
        print(f"Found position: x={x}, y={y}")
        break

Img = Image.open('a.png')
region = (x, y, 1300, 760)

time.sleep(2)

def LookForInputAndClick(InputImg):
    try:
        Input = pyautogui.locateOnScreen(image = InputImg, region = region, grayscale = True, confidence = 0.85)
        if Input is not None:
            print(f"Found Input at position: left={Input.left}, top={Input.top}")
            Click((Input.left + 14, Input.top + 44))
    except:
        pass

while not keyboard.is_pressed('q'):
    time.sleep(0.0001)
    LookForInputAndClick(Img)