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
    # bank
    pyautogui.moveTo(380, 463)
    click_random_position(380, 463, 3, 3)

    time.sleep(.8)

    # right click item 2
    pyautogui.moveTo(641, 719)
    time.sleep(.4)
    right_click_random_position(641, 719, 3, 3)
    time.sleep(.9)

    # click item 2 deposit all
    pyautogui.moveTo(583, 819)
    time.sleep(.4)
    click_random_position(583, 819, 2, 1)
    time.sleep(.5)

    # right click bank item
    pyautogui.moveTo(442, 142)
    time.sleep(.4)
    right_click_random_position(442, 142, 3, 1)
    time.sleep(.5)

    # click select all bank item
    pyautogui.moveTo(406, 243)
    time.sleep(.1)
    click_random_position(406, 243, 2, 1)
    time.sleep(.5)

    # close bank
    click_random_position(505, 65, 3, 3)
    time.sleep(.5)

def combine():
    # for i in range(14):
    click_random_position(602, 718, 3, 3)
    time.sleep(.3)
    click_random_position(641, 719, 3, 3)
    time.sleep(1)
    pyautogui.keyDown('3')
    pyautogui.keyUp('3')
    time.sleep(1)
    pyautogui.keyDown('3')
    pyautogui.keyUp('3')
    time.sleep(1)
    pyautogui.keyDown('2')
    pyautogui.keyUp('2')


while True:
    rebank()
    combine()
    time.sleep(48)
