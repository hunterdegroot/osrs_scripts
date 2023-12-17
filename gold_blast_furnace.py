import time
import random
import pyautogui
from PIL import ImageGrab
import datetime


check_interval = 15
click_delay_min = 0.03  # 30ms
click_delay_max = 0.4   # 200ms

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


def rebank():
    pyautogui.moveTo(643, 721)
    time.sleep(.4)
    right_click_random_position(643, 721, 3, 3)
    time.sleep(.4)
    pyautogui.moveTo(627, 820)
    time.sleep(.4)
    click_random_position(627, 820, 2, 1)

    pyautogui.moveTo(439, 702)
    time.sleep(.4)
    right_click_random_position(439, 702, 3, 3)
    time.sleep(.4)
    pyautogui.moveTo(421, 803)
    time.sleep(.4)
    click_random_position(421, 803, 2, 1)

    time.sleep(.01)
    click_random_position(500, 66, 2, 1)

    # time.sleep(1)
    # click_random_position(603, 721, 2, 2)

    time.sleep(1)
    pyautogui.moveTo(16, 686)
    time.sleep(.4)
    click_random_position(16, 686, 2, 2)
    
    time.sleep(14)
    pyautogui.keyDown('1')
    pyautogui.keyUp('1')

    time.sleep(5)
    click_random_position(603, 721, 2, 2)

    time.sleep(1)
    pyautogui.moveTo(502, 599)
    time.sleep(.4)
    click_random_position(502, 599, 2, 2)

    time.sleep(8)
    pyautogui.keyDown('1')
    pyautogui.keyUp('1')
 
    click_random_position(603, 721, 2, 2)

    time.sleep(1)
    pyautogui.moveTo(601, 327)
    time.sleep(.4)
    click_random_position(601, 327, 2, 2)

    time.sleep(9)
while True:
    rebank()