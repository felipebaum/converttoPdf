import time
import selenium


lista = []
f = open('mdfes.txt', 'r')
for c in f:
    lista.append(c)

import webbrowser
for c in lista:
    webbrowser.open(f"{c}")

"""from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

"""