import pyautogui
import keyboard

def get_cursor_info():
    x, y = pyautogui.position()
    r, g, b = pyautogui.pixel(x, y)  # Unpack RGB values
    hex_color = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return x, y, hex_color

def main():
    print("Press the '1' key to capture cursor info and hex color. Press 'Esc' to exit.")
    while True:
        if keyboard.is_pressed("1"):
            x, y, hex_color = get_cursor_info()
            print(f"Cursor Position: ({x}, {y}), Hex Color: {hex_color}")

        if keyboard.is_pressed("esc"):
            print("Program terminated.")
            break

if __name__ == "__main__":
    main()
