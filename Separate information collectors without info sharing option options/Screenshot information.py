from PIL import ImageGrab
import time

screenshot_information = "screenshot.png"

file_path = "C:\Info-logger\Logged_information"
extend = "\\"
file_merge = file_path + extend

def screenshot():
    time.sleep(2)
    im = ImageGrab.grab()
    im.save(file_path + extend + screenshot_information)

screenshot()