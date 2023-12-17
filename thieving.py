import time
import random
import pyautogui
from PIL import ImageGrab

check_interval = 15
click_delay_min = 0.03  # 30ms
click_delay_max = 0.05   # 200ms


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
    click_random_position(456, 821, 5, 5)
    time.sleep(1.2)

    # right click item 1
    right_click_random_position(386, 698, 2, 2)
    time.sleep(1.2)

    # specific withdraw item 1
    click_random_position(351, 770, 2, 2)
    time.sleep(1.2)

    # right click item 2
    right_click_random_position(436, 699, 2, 2)
    time.sleep(1.2)

    # specific withdraw item 2
    click_random_position(396, 770, 2, 2)
    time.sleep(1.2)

    # close bank
    click_random_position(496, 64, 3, 3)
    time.sleep(1.2)


def check_hex_code_in_area(x, y, width, height):
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
    pixels = screenshot.load()

    for i in range(width):
        for j in range(height):
            pixel_color = pixels[i, j]
            if "#{:02x}{:02x}{:02x}".format(*pixel_color[:3]) == "#ff0000":
                return True

    return False


def combine():
    # for i in range(14):
    click_random_position(
        bag_positions['14']['x'][0], bag_positions['14']['y'][0], 3, 3)
    time.sleep(.6)
    click_random_position(
        bag_positions['28']['x'][0], bag_positions['28']['y'][0], 3, 3)
    time.sleep(2)
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')

break_flag = False
while True:
    break_flag = False
    pyautogui.moveTo(355, 497)
    time.sleep(.2)

    #bonk
    right_click_random_position(355, 497, 2, 2)
    time.sleep(.2)
    click_random_position(305, 581, 3, 3)
    time.sleep(1)

    for i in range(8):
        if (check_hex_code_in_area(359, 492, 39, 39)):
            click_random_position(411, 533, 3, 3)
            break
        time.sleep(.1)

    else:
        while (True):
            #loot
            pyautogui.moveTo(379, 492)
            time.sleep(.2)
            click_random_position(379, 492, 2, 1)
            time.sleep(.1)
            click_random_position(379, 492, 2, 1)
            # time.sleep(.2)
            # click_random_position(371, 548, 3, 2)

            #bonk
            pyautogui.moveTo(379, 494)
            time.sleep(.1)
            right_click_random_position(379, 494, 2, 1)
            time.sleep(.2)
            click_random_position(345, 579, 3, 2)
            time.sleep(.1)

            for i in range(3):
                if (check_hex_code_in_area(359, 492, 39, 39)):
                    click_random_position(411, 533, 3, 2)
                    break_flag = True
                    break
                time.sleep(.1)

            if(break_flag):
                break

    time.sleep(6)
