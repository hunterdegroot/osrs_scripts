import time
import random
import pyautogui
from PIL import ImageGrab
import time


check_interval = 15
click_delay_min = 0.21144  # 30ms
click_delay_max = 0.242   # 200ms


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
    target_x = random.randint(x, x + width)
    target_y = random.randint(y, y + height)

    click_delay = random.uniform(click_delay_min, click_delay_max)
    pyautogui.moveTo(target_x, target_y)
    time.sleep(.3)
    time.sleep(click_delay)
    pyautogui.click(target_x, target_y)


bag = [
    (592, 723),
    (633, 722),
    (675, 724),
    (718, 723),

    (591, 759),
    (634, 761),
    (677, 760),
    (718, 760),

    (592, 796),
    (633, 796),
    (675, 796),
    (718, 796),

    (591, 832),
    (634, 832),
    (677, 832),
    (718, 832),

    (592, 870),
    (633, 870),
    (675, 870),
    (718, 870),

    (591, 905),
    (634, 905),
    (677, 905),
    (718, 905),

    (598, 934),
    (633, 940),
    (675, 940),
    (718, 940)
]


def shift_left_click(x, y):
    click_delay = random.uniform(click_delay_min, click_delay_max)
    pyautogui.keyDown('shift')  # Hold the Shift key
    pyautogui.moveTo(x, y)
    time.sleep(click_delay)
    pyautogui.click(x, y)
    pyautogui.keyUp('shift')  # Hold the Shift key



def drop():
    for each in bag:
        shift_left_click(each[0], each[1])

def relog():
    pyautogui.moveTo(746, 35)
    time.sleep(1.5)
    click_random_position(746, 35, 2, 2)
    time.sleep(2)
    pyautogui.moveTo(655, 920)
    time.sleep(1.5)
    click_random_position(655, 920, 2, 2)
    time.sleep(2)
    pyautogui.moveTo(377, 289)
    time.sleep(1.5)
    click_random_position(377, 289, 2, 2)
    time.sleep(15)
    pyautogui.moveTo(389, 361)
    time.sleep(1.5)
    click_random_position(389, 361, 2, 2)
    time.sleep(2)
    pyautogui.keyDown('up')
    time.sleep(random.uniform(1,1.1))
    pyautogui.keyUp('up')
    pyautogui.keyDown('f4')
    pyautogui.keyUp('f4')
    time.sleep(1)


while True:
    relog()
    for i in range(100):
        start = time.time()
        for b in range(8):
            click_random_position(150, 597, 3, 3)
            time.sleep(1.7)
            click_random_position(367, 811, 3, 3)
            time.sleep(1.7)
            click_random_position(606, 603, 3, 3)
            time.sleep(1.7)
        drop()
        end = time.time()
        print(end - start)

