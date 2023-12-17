import time
import random
import pyautogui
from PIL import ImageGrab

click_delay_min = 0.03  # 30ms
click_delay_max = 0.2   # 200ms


def click_random_position(x, y, width, height):
    target_x = random.randint(x, x + width)
    target_y = random.randint(y, y + height)

    click_delay = random.uniform(click_delay_min, click_delay_max)
    time.sleep(click_delay)
    pyautogui.click(target_x, target_y)

# while True:
for i in range (134):
    click_random_position(600, 712, 0, 0)
    time.sleep(.1)
    click_random_position(641, 712, 0, 0)
    time.sleep(1.6)
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')
    time.sleep(13.5)
