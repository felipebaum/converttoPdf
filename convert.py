import time
import webbrowser
import pyautogui

lista = []
f = open('mdfes.txt', 'r')
for c in f:
    lista.append(c)
    webbrowser.open(c)
    time.sleep(5)
    pyautogui.press("ester")
