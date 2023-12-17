import pyautogui
from PIL import Image

def find_closest_cyan_pixel(image, target_color=(0, 255, 255), tolerance=50, search_area=None):
    width, height = image.size
    closest_pixel = None
    closest_distance = float('inf')

    start_x, start_y, end_x, end_y = search_area if search_area else (0, 0, width, height)

    for x in range(start_x, end_x):
        for y in range(start_y, end_y):
            pixel_color = image.getpixel((x, y))
            distance = sum(abs(pixel_color[i] - target_color[i]) for i in range(3))
            
            if distance <= tolerance and distance < closest_distance:
                closest_pixel = (x, y)
                closest_distance = distance
                
    return closest_pixel

def main():
    target_position = (394, 527)
    search_area = (8, 241, 746, 845)
    
    screenshot = pyautogui.screenshot()
    closest_pixel_relative = find_closest_cyan_pixel(screenshot, target_color=(0, 255, 255), tolerance=50, search_area=search_area)
    
    if closest_pixel_relative:
        target_x, target_y = target_position
        x_relative, y_relative = closest_pixel_relative
        x_absolute = search_area[0] + x_relative
        y_absolute = search_area[1] + y_relative
        pyautogui.click(x_absolute, y_absolute)
        print(f"Clicked at pixel ({x_absolute}, {y_absolute})")
    else:
        print("No suitable pixel found.")

if __name__ == "__main__":
    main()