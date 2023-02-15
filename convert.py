import time
import webbrowser
import pyautogui

lista = []
contador=2483
f = open('mdfes.txt', 'r')
for c in f:
    lista.append(c)
    webbrowser.open(c)
    time.sleep(45)
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.write(f"Mdfe{contador}")
    pyautogui.press("enter")
    contador+=1
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('w')
    time.sleep(3)
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('w')

