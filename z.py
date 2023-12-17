import time
import random
import pyautogui
from PIL import ImageGrab

click_delay_min = 0.12  # 30ms
click_delay_max = 0.2   # 200ms
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


def click_random_position(x, y, width, height):
    target_x = random.randint(x, x + width)
    target_y = random.randint(y, y + height)

    click_delay = random.uniform(click_delay_min, click_delay_max)
    pyautogui.moveTo(target_x, target_y)
    time.sleep(.3)
    time.sleep(click_delay)
    pyautogui.click(target_x, target_y)


def right_click_random_position(x, y, width, height):
    target_x = random.randint(x, x + width)
    target_y = random.randint(y, y + height)

    click_delay = random.uniform(click_delay_min, click_delay_max)
    time.sleep(click_delay)
    pyautogui.click(target_x, target_y, 1, 0, 'right')




def check_hex_code_in_area(x, y, width, height):
    screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
    pixels = screenshot.load()

    for i in range(width):
        for j in range(height):
            pixel_color = pixels[i, j]
            if abs(pixel_color[0] - 73) < 10 and abs(pixel_color[1] - 103) < 10 and abs(pixel_color[2] - 31) < 10:
                return True

    return False


def out():
    return check_hex_code_in_area(392, 528, 416 - 392, 550 - 528)

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
    pyautogui.keyDown('w')
    time.sleep(random.uniform(1,1.1))
    pyautogui.keyUp('w')

def repair():
    click_random_position(637, 937, 1, 1)
    time.sleep(8)
    click_random_position(677, 981, 1, 1)
    time.sleep(.5)
    click_random_position(655, 720, 2, 2)
    time.sleep(.5)
    click_random_position(658, 797, 2, 2)
    time.sleep(.5)
    click_random_position(658, 836, 2, 2)
    time.sleep(.5)
    click_random_position(603, 794, 2, 2)
    time.sleep(.5)
    pyautogui.keyDown('1')
    pyautogui.keyUp('1')
    time.sleep(.5)
    right_click_random_position(593, 721, 2, 1)
    time.sleep(.5)
    click_random_position(522, 778, 2, 2)
    time.sleep(.5)
    pyautogui.moveTo(483, 361)
    time.sleep(1)
    click_random_position(483, 361, 2, 2)
    time.sleep(10)
    pyautogui.keyDown('2')
    pyautogui.keyUp('2')
    time.sleep(2)
    click_random_position(bag[0][0], bag[0][1], 1, 1)
    time.sleep(.6)
    click_random_position(bag[1][0], bag[1][1], 1, 1)
    time.sleep(.6)
    click_random_position(bag[2][0], bag[2][1], 1, 1)
    time.sleep(.6)
    click_random_position(bag[3][0], bag[3][1], 1, 1)
    time.sleep(2)
    pyautogui.moveTo(284, 795)
    time.sleep(1)
    click_random_position(284, 795, 2, 2)
    time.sleep(6)

def tp_nmz():
    right_click_random_position(737, 893, 1, 1)
    time.sleep(.2)
    click_random_position(737, 893, 1, 1)
    time.sleep(.5)
    pyautogui.keyDown('2')
    pyautogui.keyUp('2')
    time.sleep(.5)
    pyautogui.moveTo(645, 1016)
    time.sleep(.5)
    click_random_position(645, 1016, 1, 1)
    time.sleep(.5)
    pyautogui.moveTo(737, 753)
    time.sleep(.5)
    click_random_position(737, 753, 1, 1)
    time.sleep(.5)
    pyautogui.moveTo(738, 825)
    time.sleep(.5)
    click_random_position(738, 825, 1, 1)
    time.sleep(.5)
    pyautogui.moveTo(700, 851)
    time.sleep(.5)
    click_random_position(700, 851, 1, 1)
    time.sleep(2)
    pyautogui.moveTo(713, 947)
    time.sleep(.5)
    click_random_position(713, 947, 2, 2)
    time.sleep(20)
    click_random_position(353, 771, 2, 2)
    time.sleep(9)
    if not out():
        exit()
    # click_random_position(603, 794, 2, 2)


def resupply():
    pyautogui.moveTo(405, 414)
    time.sleep(1.5)
    click_random_position(405, 414, 1, 1)
    time.sleep(6)
    pyautogui.moveTo(257, 342)
    time.sleep(1.5)
    click_random_position(257, 342, 1, 1)
    time.sleep(.5)
    pyautogui.moveTo(198, 465)
    time.sleep(1.5)
    right_click_random_position(198, 465, 1, 0)
    time.sleep(.5)
    pyautogui.moveTo(160, 552)
    time.sleep(1.5)
    click_random_position(160, 552, 1, 1)
    time.sleep(2)
    pyautogui.keyDown('2')
    pyautogui.keyUp('2')
    time.sleep(random.uniform(1,1.1))
    pyautogui.keyDown('2')
    pyautogui.keyUp('2')
    time.sleep(random.uniform(1,1.1))
    pyautogui.keyDown('5')
    pyautogui.keyUp('5')
    time.sleep(random.uniform(1,1.1))
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    time.sleep(.5)
    pyautogui.moveTo(264, 465)
    time.sleep(1.5)
    right_click_random_position(264, 465, 1, 0)
    time.sleep(.5)
    pyautogui.moveTo(214, 551)
    time.sleep(1.5)
    click_random_position(214, 551, 1, 1)
    time.sleep(2)
    pyautogui.keyDown('2')
    pyautogui.keyUp('2')
    time.sleep(random.uniform(1,1.1))
    pyautogui.keyDown('2')
    pyautogui.keyUp('2')
    time.sleep(random.uniform(1,1.1))
    pyautogui.keyDown('5')
    pyautogui.keyUp('5')
    time.sleep(random.uniform(1,1.1))
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    time.sleep(.5)
    click_random_position(497, 318, 1, 1)

    pyautogui.moveTo(69, 581)
    time.sleep(1.5)
    right_click_random_position(69, 581, 1, 0)
    time.sleep(.5)
    pyautogui.moveTo(20, 622)
    time.sleep(1.5)
    click_random_position(20, 622, 1, 1)
    time.sleep(8)
    pyautogui.keyDown('2')
    pyautogui.keyUp('2')
    time.sleep(random.uniform(1,1.1))
    pyautogui.keyDown('1')
    pyautogui.keyUp('1')
    time.sleep(random.uniform(1,1.2))
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')

    pyautogui.moveTo(340, 481)
    time.sleep(1.5)
    right_click_random_position(340, 481, 1, 0)
    time.sleep(.5)
    pyautogui.moveTo(266, 522)
    time.sleep(1.5)
    click_random_position(266, 522, 1, 1)
    time.sleep(8)
    pyautogui.keyDown('9')
    pyautogui.keyUp('9')
    time.sleep(random.uniform(1,1.2))
    pyautogui.keyDown('9')
    pyautogui.keyUp('9')
    time.sleep(random.uniform(.89,1.3))
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')

    pyautogui.moveTo(499, 519)
    time.sleep(1.5)
    click_random_position(499, 519, 1, 1)
    time.sleep(4)
    pyautogui.moveTo(412, 479)
    time.sleep(1.5)
    click_random_position(412, 479, 1, 1)
    time.sleep(4)

def redream():
    pyautogui.moveTo(378, 491)
    time.sleep(1.5)
    right_click_random_position(378, 491, 1, 0)
    time.sleep(2.5)
    pyautogui.moveTo(330, 533)
    time.sleep(1.5)
    click_random_position(330, 533, 1, 1)
    time.sleep(2.5)
    pyautogui.keyDown('4')
    pyautogui.keyUp('4')
    time.sleep(random.uniform(3,3.2))
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')
    time.sleep(random.uniform(3.89,4.3))
    pyautogui.keyDown('1')
    pyautogui.keyUp('1')
    time.sleep(3.5)



def start():
    click_random_position(bag[25][0], bag[25][1], 1, 1)
    time.sleep(.6)
    click_random_position(bag[25][0], bag[25][1], 1, 1)
    time.sleep(.6)
    click_random_position(bag[25][0], bag[25][1], 1, 1)
    time.sleep(.6)
    click_random_position(bag[25][0], bag[25][1], 1, 1)

    time.sleep(.6)
    click_random_position(bag[26][0], bag[26][1], 1, 1)
    time.sleep(.6)
    click_random_position(bag[26][0], bag[26][1], 1, 1)
    time.sleep(.6)
    click_random_position(bag[26][0], bag[26][1], 1, 1)
    time.sleep(.6)
    click_random_position(bag[26][0], bag[26][1], 1, 1)

    time.sleep(.6)
    click_random_position(bag[27][0], bag[27][1], 1, 1)
    time.sleep(.6)
    click_random_position(bag[27][0], bag[27][1], 1, 1)
    time.sleep(.6)
    click_random_position(bag[27][0], bag[27][1], 1, 1)
    time.sleep(.6)
    click_random_position(bag[27][0], bag[27][1], 1, 1)

    index = 0
    row = 0
    rowCount = 0
    while row != 6:
        pyautogui.moveTo(593, 123)
        time.sleep(1.2)
        click_random_position(593, 123, 1, 1)
        time.sleep(.3)
        click_random_position(593, 123, 1, 1)

        if index % 6 == 0:
            if rowCount % 4 == 0 and rowCount != 0:
                row += 1
            rowCount += 1
            if row == 0:
                click_random_position(bag[0][0], bag[0][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[7][0], bag[7][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[8][0], bag[8][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[9][0], bag[9][1], 1, 1)
                time.sleep(7)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
            if row == 1:
                click_random_position(bag[1][0], bag[1][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[10][0], bag[10][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[11][0], bag[11][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[12][0], bag[12][1], 1, 1)
                time.sleep(7)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
            if row == 2:
                click_random_position(bag[2][0], bag[2][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[13][0], bag[13][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[14][0], bag[14][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[15][0], bag[15][1], 1, 1)
                time.sleep(7)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
            if row == 3:
                click_random_position(bag[3][0], bag[3][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[16][0], bag[16][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[17][0], bag[17][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[18][0], bag[18][1], 1, 1)
                time.sleep(7)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
            if row == 4:
                click_random_position(bag[4][0], bag[4][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[19][0], bag[19][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[20][0], bag[20][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[21][0], bag[21][1], 1, 1)
                time.sleep(7)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
                time.sleep(.6)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
            if row == 5:
                click_random_position(bag[5][0], bag[5][1], 1, 1)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
                click_random_position(bag[24][0], bag[24][1], 1, 1)
                time.sleep(20)
                row+=1
                # time.sleep(.6)
                # click_random_position(bag[23][0], bag[23][1], 1, 1)
            # if row == 7:
            #     click_random_position(bag[15][0], bag[15][1], 1, 1)
            #     time.sleep(.6)
            #     click_random_position(bag[19][0], bag[19][1], 1, 1)
            #     time.sleep(.6)
            #     click_random_position(bag[23][0], bag[23][1], 1, 1)
            #     # time.sleep(.6)
            #     # click_random_position(bag[23][0], bag[23][1], 1, 1)
            # if row == 8:
            #     click_random_position(bag[26][0], bag[26][1], 1, 1)
            #     time.sleep(.6)
            # if row == 9:
            #     click_random_position(bag[27][0], bag[27][1], 1, 1)
            #     time.sleep(.6)
            # if row == 10:
            #     for i in range(5):
            #         click_random_position(bag[24][0], bag[24][1], 1, 1)
            #         time.sleep(.6)
        # elif not out():
        #     click_random_position(bag[24][0], bag[24][1], 1, 1)

        pyautogui.moveTo(593, 123)
        time.sleep(1.2)
        click_random_position(593, 123, 1, 1)
        time.sleep(.3)
        click_random_position(593, 123, 1, 1)

        index += 1
        time.sleep(41.5)

for i in range(7):
    relog()
    pyautogui.keyDown('1')
    pyautogui.keyUp('1')
    time.sleep(1)
    # repair()
    # tp_nmz()
    redream()
    resupply()
    start()
    time.sleep(22)




