import time
import random
import pyautogui

click_delay_min = 0.03  # 30ms
click_delay_max = 0.2   # 200ms

def click_random_position(x, y, width, height):
    target_x = random.randint(x, x + width)
    target_y = random.randint(y, y + height)

    click_delay = random.uniform(click_delay_min, click_delay_max)
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
    
    (592, 940),
    (633, 940),
    (675, 940),
    (718, 940)
]

for (x, y) in bag:
    for i in range (4):
        time.sleep(42)
        click_random_position(x, y, 0, 0)
        click_random_position(x, y, 0, 0)

