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

# Cadastrando 1 Produto


for linha in tabela.index:
    pyautogui.click(x=2802, y=-1237)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press('tab')

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press('tab')

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press('tab')

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press('tab')

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press('tab')

    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)


    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(10000)









