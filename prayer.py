import time
import random
import pyautogui
from PIL import ImageGrab

click_delay_min = 0.03  # 30ms
click_delay_max = 0.2   # 200ms
def find_pixel_with_color(hex_color):
    screen_width, screen_height = pyautogui.size()
    for x in range(screen_width):
        for y in range(screen_height):
            pixel_color = pyautogui.pixel(x, y)
            if '#{:02X}{:02X}{:02X}'.format(*pixel_color) == hex_color:
                return x, y
    return None, None

def move_mouse_to_pixel(hex_color):
    x, y = find_pixel_with_color(hex_color)
    if x is not None and y is not None:
        pyautogui.moveTo(x, y)
        print(f"Moved mouse to pixel with color {hex_color} at ({x}, {y})")
    else:
        print(f"Pixel with color {hex_color} not found on the screen")

target_hex_color = "#c1885a" 

def right_click_random_position(x, y, width, height):
    target_x = random.randint(x, x + width)
    target_y = random.randint(y, y + height)

    click_delay = random.uniform(click_delay_min, click_delay_max)
    time.sleep(click_delay)
    pyautogui.click(target_x, target_y, .16, .1, 'right')

def click_random_position(x, y, width, height):
    target_x = random.randint(x, x + width)
    target_y = random.randint(y, y + height)

    click_delay = random.uniform(click_delay_min, click_delay_max)
    time.sleep(click_delay)
    pyautogui.click(target_x, target_y)

def a():
    # click_random_position(640, 716, 2, 2)
    # time.sleep(.2)
    # click_random_position(299, 820, 2, 2)
    # time.sleep(3)
    # pyautogui.keyDown('3')
    # pyautogui.keyUp('3')
    # right_click_random_position(435, 324, 1, 3)
    # time.sleep(.2)
    # click_random_position(380, 381, 1, 1)
    # time.sleep(5)
    # click_random_position(728, 930, 2, 2)
    # time.sleep(4)

    for i in range(25):
        pyautogui.moveTo(727, 93)
        time.sleep(.1)
        click_random_position(727, 931, 1, 1)
        pyautogui.moveTo(386, 493)
        time.sleep(.1)
        click_random_position(386, 493, 2, 2)

    # click_random_position(135, 536, 2, 2)
    # time.sleep(5)


from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    if button == button.middle and pressed:
        a()

# Create a listener that waits for mouse events
with Listener(on_click=on_click) as listener:
    listener.join()

# while True:
