import pyautogui
import time
import random
from PIL import ImageGrab

# Hex color code to match (#ff00ff)
target_color = (255, 0, 255)
# Time interval in seconds
interval = 10

def check_hex_code_in_area(x, y, width, height):
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
    pixels = screenshot.load()

    for i in range(width):
        for j in range(height):
            pixel_color = pixels[i, j]
            if "#{:02x}{:02x}{:02x}".format(*pixel_color[:3]) == "#f00fff3":
                print(str(i) + " " + str(j))
                return x + i, y + j

while True:
    nearest_pixel = check_hex_code_in_area(43, 295, 580, 500)
    if nearest_pixel:
        click_x, click_y = nearest_pixel

        buffer = random.uniform(0.0, 0.3)

        pyautogui.moveTo(click_x, click_y)
        pyautogui.click(click_x, click_y)
        time.sleep(interval - buffer)
