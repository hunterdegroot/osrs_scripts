import time
import random
import pyautogui
from PIL import ImageGrab
from datetime import datetime, timedelta

click_delay_min = 0.03  # 30ms
click_delay_max = 0.2   # 200ms


def click_random_position(x, y, width, height):
    target_x = random.randint(x, x + width)
    target_y = random.randint(y, y + height)

    click_delay = random.uniform(click_delay_min, click_delay_max)
    time.sleep(click_delay)
    pyautogui.rightClick(target_x, target_y)
    pyautogui.rightClick(target_x, target_y)

    click_delay = random.uniform(click_delay_min, click_delay_max)
    time.sleep(click_delay)
    pyautogui.moveTo(target_x, target_y + 25, .2)
    pyautogui.click()


def check_hex_code_in_area3(x, y, width, height):
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
    pixels = screenshot.load()

    for i in range(width):
        for j in range(height):
            pixel_color = pixels[i, j]
            if "#{:02x}{:02x}{:02x}".format(*pixel_color[:3]) == "#eff3a1":
                return True

    return False


def check_hex_code_in_area(x, y, width, height):
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
    pixels = screenshot.load()

    for i in range(width):
        for j in range(height):
            pixel_color = pixels[i, j]
            if "#{:02x}{:02x}{:02x}".format(*pixel_color[:3]) == "#a6954e":
                return True

    return False

def logged_out():
    return check_hex_code_in_area3(186, 109,120,100)

one_hour_ago = datetime.now() - timedelta(hours=1)


while True:
    if logged_out():
        current_time = datetime.now()
        time_difference = current_time - one_hour_ago
        one_hour_ago = datetime.now()

        chopping = False

        time.sleep(2)
        pyautogui.click(383, 324)
        time.sleep(2)
        pyautogui.click(386, 281)
        time.sleep(10)
        pyautogui.click(393, 357)
        time.sleep(2)
        pyautogui.keyDown('w')
        time.sleep(random.uniform(1,1.1))
        pyautogui.keyUp('w')
        pyautogui.keyDown('2')  # Hold the Shift key
        pyautogui.keyUp('2')


    current_time = datetime.now()

    time_difference = current_time - one_hour_ago

    threshold = timedelta(hours=5, minutes=58)


    if not check_hex_code_in_area(412,555,35,30):  # 3600 seconds = 1 hour
            break
    if not time_difference >= threshold:
        pyautogui.moveTo(238, 123)
        time.sleep(.2)
        click_random_position(238, 123, 0, 0)
        time.sleep(14)

        pyautogui.moveTo(271, 189)
        time.sleep(.2)
        click_random_position(271, 189, 0, 0)
        time.sleep(14)

        pyautogui.moveTo(416, 853)
        time.sleep(.2)
        click_random_position(416, 853, 0, 0)
        time.sleep(8)

        pyautogui.moveTo(388, 854)
        time.sleep(.2)
        click_random_position(388, 854, 0, 0)
        time.sleep(8)

        pyautogui.moveTo(538, 857,)
        time.sleep(.2)
        click_random_position(538, 857, 0, 0)
        time.sleep(13)

        pyautogui.moveTo(533, 778)
        time.sleep(.2)
        click_random_position(533, 778, 0, 0)
        time.sleep(7)

        pyautogui.moveTo(441, 505)
        time.sleep(.2)
        click_random_position(441, 505, 0, 0)
    time.sleep(350)
    if not logged_out():
        time.sleep(250)





