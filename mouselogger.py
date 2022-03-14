import mouse
import pyautogui

click  = 0    # 몇 번째 클릭인지저장할 변수  

while True:
    if mouse.is_pressed("left") or mouse.is_pressed("right"):
        click += 1
        pos = mouse.get_position()
        pyautogui.screenshot('1.png')