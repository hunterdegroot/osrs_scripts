import time
import random
import pyautogui
from PIL import ImageGrab
from datetime import datetime, timedelta

click_delay_min = 0.03  # 30ms
click_delay_max = 0.2   # 200ms

def check_hex_code_in_area3(x, y, width, height):
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
    pixels = screenshot.load()

    for i in range(width):
        for j in range(height):
            pixel_color = pixels[i, j]
            if "#{:02x}{:02x}{:02x}".format(*pixel_color[:3]) == "#eff3a1" or "#{:02x}{:02x}{:02x}".format(*pixel_color[:3]) == "#e2e238":
                return True

    return False


def click_random_position(x, y, width, height):
    target_x = random.randint(x, x + width)
    target_y = random.randint(y, y + height)

    click_delay = random.uniform(click_delay_min, click_delay_max)
    time.sleep(click_delay)
    pyautogui.click(target_x, target_y)

def logged_out():
    return check_hex_code_in_area3(186, 109,120,100)

one_hour_ago = datetime.now() - timedelta(hours=1)

for i in range (1588):
    # if logged_out():
    #     current_time = datetime.now()
    #     time_difference = current_time - one_hour_ago
    #     one_hour_ago = datetime.now()

    #     chopping = False

    #     time.sleep(2)
    #     pyautogui.click(383, 324)
    #     time.sleep(2)
    #     pyautogui.click(386, 281)
    #     time.sleep(10)
    #     pyautogui.click(393, 357)
    #     time.sleep(2)
    #     pyautogui.keyDown('3')
    #     pyautogui.keyUp('3')
    #     time.sleep(random.uniform(1,1.1))
    #     pyautogui.keyDown('4')  # Hold the Shift key
    #     pyautogui.keyUp('4')
    click_random_position(739, 797, 0, 0)
    time.sleep(.4)
    click_random_position(739, 797, 0, 0)
    time.sleep(2.6)


