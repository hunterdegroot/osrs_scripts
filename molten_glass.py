import time
import random
import pyautogui
from PIL import ImageGrab

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
    # deposit
    click_random_position(456, 821, 5, 5)
    time.sleep(1.2)

    # right click item 1
    pyautogui.moveTo(386, 698)
    time.sleep(.2)
    right_click_random_position(386, 698, 2, 1)
    time.sleep(1.2)

    # specific withdraw item 1
    pyautogui.moveTo(351, 770)
    time.sleep(.2)
    click_random_position(351, 770, 2, 1)
    time.sleep(1.2)

    # right click item 2
    pyautogui.moveTo(436, 699)
    time.sleep(.2)
    right_click_random_position(436, 699, 2, 1)
    time.sleep(1.2)

    # specific withdraw item 2
    pyautogui.moveTo(396, 770)
    time.sleep(.2)
    click_random_position(396, 770, 2, 1)
    time.sleep(1.2)

    # close bank
    click_random_position(496, 64, 3, 3)
    time.sleep(1.2)


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
    click_random_position(bag_positions['14']['x'][0], bag_positions['14']['y'][0], 3, 3)
    time.sleep(.6)
    click_random_position(bag_positions['28']['x'][0], bag_positions['28']['y'][0], 3, 3)
    time.sleep(2)
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')


while True:
    rebank()
    click_random_position(170, 691, 3, 3)
    time.sleep(4)
    pyautogui.moveTo(189, 530)
    time.sleep(.4)
    click_random_position(189, 530, 3, 3)
    time.sleep(4)
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')
    time.sleep(18)
    pyautogui.moveTo(708, 357)
    time.sleep(.4)
    click_random_position(708, 357, 3, 3)
    time.sleep(5)

