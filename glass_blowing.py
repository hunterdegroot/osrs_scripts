import time
import random
import pyautogui
from PIL import ImageGrab
import datetime

check_interval = 15
click_delay_min = 0.03  # 30ms
click_delay_max = 0.2   # 200ms


def click_random_position(x, y, width, height):
    target_x = random.randint(x, x + width)
    target_y = random.randint(y, y + height)

    click_delay = random.uniform(click_delay_min, click_delay_max)
    time.sleep(click_delay)
    pyautogui.click(target_x, target_y)

    # time.sleep(click_delay)
    # pyautogui.click(target_x, target_y)


def right_click_random_position(x, y, width, height):
    target_x = random.randint(x, x + width)
    target_y = random.randint(y, y + height)

    click_delay = random.uniform(click_delay_min, click_delay_max)
    time.sleep(click_delay)
    pyautogui.click(target_x, target_y, 1, 0, 'right')

    # time.sleep(click_delay)
    # pyautogui.right(target_x, target_y)


def lvl():
    screenshot = ImageGrab.grab(bbox=(190, 978, 332, 987))
    pixels = screenshot.load()
    for i in range(332-190):
        for j in range(987-978):
            pixel_color = pixels[i, j]
            if "#{:02x}{:02x}{:02x}".format(*pixel_color[:3]) == "#0000ff":
                return True

    return False


def click_continue():
    target_x = random.randint(190, 332)  # Random position within the square
    target_y = random.randint(978, 987)

    click_delay = random.uniform(click_delay_min, click_delay_max)
    time.sleep(click_delay)
    pyautogui.click(target_x, target_y)


bag_positions = {
    "14": {
        'x': [633, 647],
        'y': [821, 833]
    },
    "28": {
        'x': [720, 731],
        'y': [926, 938]
    }
}


def rebank():
    # bank
    pyautogui.moveTo(381, 471)
    click_random_position(384, 471, 3, 3)

    time.sleep(1)
    # deposit
    pyautogui.moveTo(643, 721)
    time.sleep(.2)
    right_click_random_position(643, 721, 2, 1)
    time.sleep(.4)

    pyautogui.moveTo(624, 823)
    time.sleep(.2)
    click_random_position(624, 823, 2, 1)
    time.sleep(.4)

    # right click item 2
    pyautogui.moveTo(438, 138)
    time.sleep(.2)
    right_click_random_position(438, 138, 2, 1)
    time.sleep(.4)

    # specific withdraw item 2
    pyautogui.moveTo(415, 208)
    time.sleep(.2)
    click_random_position(415, 208, 2, 1)
    time.sleep(.4)

    # close bank
    click_random_position(496, 64, 3, 3)
    time.sleep(.4)

    # # bank
    # right_click_random_position(381, 471, 3, 3)
    # time.sleep(10)

    # click_random_position(362, 49, 3, 3)

    # time.sleep(1)
    # # deposit
    # click_random_position(452, 817, 9, 8)

    # # right click item 1
    # right_click_random_position(385, 140, 7, 3)

    # # specific withdraw item 1
    # click_random_position(317, 211, 7, 3)

    # # right click item 2
    # right_click_random_position(433, 140, 7, 3)

    # # specific withdraw item 2
    # click_random_position(375, 236, 7, 3)

    # # close bank
    # click_random_position(496, 64, 7, 3)


def combine():
    # for i in range(14):
    click_random_position(601, 716, 3, 3)
    time.sleep(.6)
    click_random_position(643, 721, 3, 3)
    time.sleep(1.2)
    pyautogui.keyDown('6')
    pyautogui.keyUp('6')


def check_hex_code_in_area(x, y, width, height):
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
    pixels = screenshot.load()

    for i in range(width):
        for j in range(height):
            pixel_color = pixels[i, j]
            if "#{:02x}{:02x}{:02x}".format(*pixel_color[:3]) == "#e2e238":
                return True

    return False


def logged_out():
    return check_hex_code_in_area(219, 93, 65, 57)

one_hour_ago = datetime.datetime.now() - datetime.timedelta(hours=1)

# while True:
for i in range(166):
    if logged_out():
        current_time = datetime.datetime.now()
        time_difference = current_time - one_hour_ago
        if not time_difference.total_seconds() >= 3600:  # 3600 seconds = 1 hour
            break
        one_hour_ago = datetime.datetime.now()

        chopping = False

        time.sleep(2)
        click_random_position(383, 324, 3, 3)
        time.sleep(2)
        click_random_position(386, 281, 3, 3)
        time.sleep(10)
        click_random_position(393, 357, 3, 3)
        time.sleep(2)
        pyautogui.keyDown('w')
        time.sleep(random.uniform(1, 1.1))
        pyautogui.keyUp('w')
        pyautogui.keyDown('2')  # Hold the Shift key
        pyautogui.keyUp('2')
    rebank()
    combine()

    time.sleep(48.2)
