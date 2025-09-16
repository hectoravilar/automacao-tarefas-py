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

#importando base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

# Cadastrando produtos
pyautogui.click(x=2802, y=-1237)

# Cadastrando produtos
codigo = "MOLO000251"
pyautogui.write(codigo)
pyautogui.press('tab')

marca = "Logitech"
pyautogui.write(marca)
pyautogui.press('tab')

tipo =  "Mouse"
pyautogui.write(tipo)
pyautogui.press('tab')

categoria = "1"
pyautogui.write(categoria)
pyautogui.press('tab')

preco_unitario = "25.95"
pyautogui.write(preco_unitario)
pyautogui.press('tab')

custo = "6.50"
pyautogui.write(custo)
pyautogui.press('tab')

obs = ""
pyautogui.write(obs)
pyautogui.press('tab')
pyautogui.press('enter')





