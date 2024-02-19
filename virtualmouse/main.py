import pyautogui
import random
import argparse


def getting_arg():
    parser = argparse.ArgumentParser(description="Welcome to Mouse bot , enter your arguments below ")
    parser.add_argument("--count" ,"--c",type=int, help="Mouse move count")
    parser.add_argument("--interval" ,"--i" ,type=int,help="Intervel between movement")
    arg = parser.parse_args()
    return arg.count , arg.interval

def main(count = 10 ,interval = 1):
    c= 0
    scrn_x ,scrn_y = pyautogui.size()
    print(scrn_x,scrn_y)
    pyautogui.FAILSAFE = False
    while c < count :
        x,y = pyautogui.position()
        print(x,y)
        pyautogui.PAUSE = 0.5
        pyautogui.moveTo(random.randint(50,scrn_x-50),random.randint(50,scrn_y-50),interval,pyautogui.easeInElastic)

        c += 1





if __name__ == "__main__":
    count , interval = getting_arg()
    if count and interval:
        main(count,interval)

    else:
        main()


