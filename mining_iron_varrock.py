import time
import random
import pyautogui
from PIL import ImageGrab

check_interval = 15
click_delay_min = 0.03  # 30ms
click_delay_max = 0.2   # 200ms


def check_hex_code_in_area(x, y, width, height):
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
    pixels = screenshot.load()

    for i in range(width):
        for j in range(height):
            pixel_color = pixels[i, j]
            if "#{:02x}{:02x}{:02x}".format(*pixel_color[:3]) == "#3d1f16":
                return True

    return False


def click_random_position(x, y, width, height):
    # Random position within the square
    target_x = random.randint(x, x + width)
    target_y = random.randint(y, y + height)
    pyautogui.moveTo(target_x, target_y)
    time.sleep(random.uniform(.4, .5))
    click_delay = random.uniform(click_delay_min, click_delay_max)
    time.sleep(click_delay)
    pyautogui.click(target_x, target_y)


bag_positions = {
    # "1": {
     #   'x': [589, 607],
    #     'y': [712, 725]
    # },
    "2": {
        'x': [633, 647],
        'y': [712, 725]
    },
    "3": {
        'x': [674, 693],
        'y': [712, 725]
    },
    "4": {
        'x': [716, 731],
        'y': [711, 725]
    },
    "5": {
        'x': [589, 607],
        'y': [751, 759]
    },
    "6": {
        'x': [633, 647],
        'y': [751, 759]
    },
    "7": {
        'x': [674, 693],
        'y': [751, 759]
    },
    "8": {
        'x': [716, 731],
        'y': [751, 759]
    },
    "9": {
        'x': [589, 607],
        'y': [786, 798]
    },
    "10": {
        'x': [633, 647],
        'y': [786, 798]
    },
    "11": {
        'x': [674, 693],
        'y': [786, 798]
    },
    "12": {
        'x': [716, 731],
        'y': [786, 798]
    },
    "13": {
        'x': [589, 607],
        'y': [821, 833]
    },
    "14": {
        'x': [633, 647],
        'y': [821, 833]
    },
    "15": {
        'x': [674, 693],
        'y': [821, 833]
    },
    "16": {
        'x': [716, 731],
        'y': [821, 833]
    },
    "17": {
        'x': [589, 607],
        'y': [856, 868]
    },
    "18": {
        'x': [633, 647],
        'y': [856, 868]
    },
    "19": {
        'x': [674, 693],
        'y': [856, 868]
    },
    "20": {
        'x': [716, 731],
        'y': [856, 868]
    },
    "21": {
        'x': [589, 607],
        'y': [891, 903]
    },
    "22": {
        'x': [633, 647],
        'y': [891, 903]
    },
    "23": {
        'x': [674, 693],
        'y': [891, 903]
    },
    "24": {
        'x': [716, 731],
        'y': [891, 903]
    },
    "25": {
        'x': [589, 607],
        'y': [926, 938]
    },
    "26": {
        'x': [633, 647],
        'y': [926, 938]
    },
    "27": {
        'x': [674, 693],
        'y': [926, 938]
    },
    "28": {
        'x': [716, 731],
        'y': [926, 938]
    }
}


def shift_left_click(x, y):
    click_delay = random.uniform(click_delay_min, click_delay_max)
    time.sleep(click_delay)
    pyautogui.keyDown('shift')  # Hold the Shift key
    pyautogui.click(x, y)
    pyautogui.keyUp('shift')  # Hold the Shift key


def drop():
    for each in bag_positions:
        e = bag_positions[each]
        shift_left_click(random.uniform(
            e['x'][0], e['x'][1]), random.uniform(e['y'][0], e['y'][1]))


while True:
    drop()
    if (not check_hex_code_in_area(356, 551, 100, 100)):
        break
    for i in range(8):
        click_random_position(412, 561, 3, 3)
        time.sleep(2.5)
        click_random_position(450, 534, 3, 3)
        time.sleep(3)
        click_random_position(326, 562, 3, 3)
        time.sleep(3.7)
