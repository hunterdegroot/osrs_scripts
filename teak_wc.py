import time
import random
import pyautogui
from PIL import ImageGrab
import datetime

check_interval = 15
click_delay_min = 0.03  # 30ms
click_delay_max = 0.2   # 200ms

def lvl_or_bag_full():
    screenshot = ImageGrab.grab(bbox=(190, 978, 332, 987))
    pixels = screenshot.load()
    for i in range(332-190):
        for j in range(987-978):
            pixel_color = pixels[i, j]
            if "#{:02x}{:02x}{:02x}".format(*pixel_color[:3]) == "#0000ff":
                return True
    
    return False

def check_hex_code_in_area(x, y, width, height):
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
    pixels = screenshot.load()

    for i in range(width):
        for j in range(height):
            pixel_color = pixels[i, j]
            hex_color = "#{:02x}{:02x}{:02x}".format(*pixel_color[:3])
            if hex_color == "#ae8b51":
                return True

    return False

def check_hex_code_in_area2(x, y, width, height):
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
    pixels = screenshot.load()

    for i in range(width):
        for j in range(height):
            pixel_color = pixels[i, j]
            if "#{:02x}{:02x}{:02x}".format(*pixel_color[:3]) == "#ab8950":
                return True

    return False

def check_hex_code_in_area3(x, y, width, height):
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
    pixels = screenshot.load()

    for i in range(width):
        for j in range(height):
            pixel_color = pixels[i, j]
            if "#{:02x}{:02x}{:02x}".format(*pixel_color[:3]) == "#e2e238":
                return True

    return False


def click_random_position(x, y, width, height):
    # Random position within the square
    target_x = random.randint(x , x + width)
    target_y = random.randint(y , y + height)
    pyautogui.moveTo(target_x,target_y)
    time.sleep(random.uniform(.4,.5))
    click_delay = random.uniform(click_delay_min, click_delay_max)
    time.sleep(click_delay)
    pyautogui.click(target_x, target_y)


bag_positions = {
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

chopping = False

def treeUp():
    return check_hex_code_in_area(600, 536, 87, 30)

def bagFull():
    return check_hex_code_in_area2(733, 929, 16, 17)

def logged_out():
    return check_hex_code_in_area3(219, 93, 65, 57)

one_hour_ago = datetime.datetime.now() - datetime.timedelta(hours=1)

#ae8b51
while True:
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
        time.sleep(random.uniform(1,1.1))
        pyautogui.keyUp('w')
        pyautogui.keyDown('2')  # Hold the Shift key
        pyautogui.keyUp('2')
    if lvl_or_bag_full():
        chopping = False
    if bagFull():
        drop()
        time.sleep(.3)
        chopping = False
    elif not chopping:
        if treeUp():
           pyautogui.moveTo(658, 536)
           time.sleep(.2)
           click_random_position(658, 536, 2, 4)
           chopping = True
    else:
        if not treeUp():
            chopping = False
    time.sleep(.5)
