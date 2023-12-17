import time
import random
import pyautogui
from PIL import ImageGrab

# Define the data dictionary with positions and sizes
data = {
    "1": {
        "1": {"pos": (407, 531), "size": (20, 22)},
        "2": {"pos": (407, 500), "size": (20, 23)},
        "3": {"pos": (560, 338), "size": (23, 15)},
        "4": {"pos": (557, 316), "size": (21, 16)},
        "5": {"pos": (555, 299), "size": (17, 12)}
    },
    "2": {
        "1": {"pos": (407, 554), "size": (18, 25)},
        "2": {"pos": (406, 523), "size": (25, 23)},
        "3": {"pos": (562, 355), "size": (22, 17)},
        "4": {"pos": (558, 335), "size": (21, 16)},
        "5": {"pos": (554, 316), "size": (22, 13)}
    },
    "3": {
        "1": {"pos": (183, 807), "size": (29, 30)},
        "2": {"pos": (188, 763), "size": (24, 28)},
        "3": {"pos": (406, 529), "size": (23, 19)},
        "4": {"pos": (407, 503), "size": (21, 16)},
        "5": {"pos": (405, 475), "size": (20, 17)}
    },
    "4": {
        "1": {"pos": (182, 838), "size": (27, 31)},
        "2": {"pos": (187, 796), "size": (20, 27)},
        "3": {"pos": (406, 555), "size": (23, 17)},
        "4": {"pos": (405, 526), "size": (22, 14)},
        "5": {"pos": (405, 497), "size": (19, 15)}
    },
    "5": {
        "1": {"pos": (175, 885), "size": (23, 32)},
        "2": {"pos": (179, 839), "size": (27, 32)},
        "3": {"pos": (407, 582), "size": (25, 20)},
        "4": {"pos": (406, 553), "size": (21, 20)},
        "5": {"pos": (406, 523), "size": (23, 19)}
    }
}

check_interval = 15
click_delay_min = 0.03  # 30ms
click_delay_max = 0.2   # 200ms


def check_hex_code_in_area(x, y, width, height):
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
    pixels = screenshot.load()

    for i in range(width):
        for j in range(height):
            pixel_color = pixels[i, j]
            if "#{:02x}{:02x}{:02x}".format(*pixel_color[:3]) == "#a65b4e":
                return True

    return False


def click_random_position(x, y, width, height):
    padding = 3
    # Random position within the square
    target_x = random.randint(x + padding, x + width - padding)
    target_y = random.randint(y + padding, y + height - padding)

    click_delay = random.uniform(click_delay_min, click_delay_max)
    time.sleep(click_delay)
    pyautogui.click(target_x, target_y)

    time.sleep(click_delay)
    pyautogui.click(target_x, target_y)


current_pos = "1"


def lvl_or_bag_full():
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


def drop_fish():
    for each in bag_positions:
        e = bag_positions[each]
        shift_left_click(random.uniform(
            e['x'][0], e['x'][1]), random.uniform(e['y'][0], e['y'][1]))


not_fishing = True

while True:
    if (lvl_or_bag_full()):
        not_fishing = True
        click_continue()
        drop_fish()

    rect = data[current_pos][current_pos]
    x, y = rect["pos"]
    width, height = rect["size"]

    # Check if the hex code is present in the rectangle (replace this with your code)
    hex_code_present = check_hex_code_in_area(x, y, width, height)
    if not hex_code_present:
        not_fishing = True
        for pos in reversed(data[current_pos].keys()) if int(current_pos) > 2 else data[current_pos]:
            rect1 = data[current_pos][pos]
            x1, y1 = rect1["pos"]
            width1, height1 = rect1["size"]
            if (check_hex_code_in_area(x1, y1, width1, height1)):
                current_pos = pos
                not_fishing = False
                click_random_position(x1, y1, width1, height1)
                time.sleep(check_interval)
                break

    elif not_fishing:
        not_fishing = False
        click_random_position(x, y, width, height)

    time.sleep(2)
