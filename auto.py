# importando bibliotecas
import pyautogui
import time 
import webbrowser

pyautogui.PAUSE = 0.5

# Abrindo navegador e entrando no site 
webbrowser.open('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
time.sleep(2)

# Fazendo Login 
# preecher email
pyautogui.click(x=2727, y=-1059) #Clicando no campo de email
pyautogui.write('hectoravllr@gmail.com') #Escrevendo email
time.sleep(1)

# preecher senha
pyautogui.press('tab') #indo para o campo de senha
pyautogui.write('123456') #Escrevendo senha

# botao de logar
pyautogui.press('tab') #Selecionando o botao de logar
pyautogui.press("enter") #Clicando no botao de logar


