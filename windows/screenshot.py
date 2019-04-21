import pyautogui
import os


def screenshot_win():
    try:
        pic = pyautogui.screenshot()
        spath = os.path.expanduser('~') + '/Desktop/screenshot.jpg'
        pic.save(spath)
    except:
        print("Unable to take screenshot.")
