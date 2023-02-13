import time
import webbrowser
import pyautogui
lista = []
f = open('mdfes.txt', 'r')
for c in f:
    lista.append(c)
    webbrowser.open_new_tab(c)
    time.sleep(5)

