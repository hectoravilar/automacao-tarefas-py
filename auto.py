# rpa para cadastro de produtos
import pandas as pd
import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

load_dotenv()

# configurando chrome headless
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

servico = ChromeService(executable_path='/usr/bin/chromedriver')
navegador = webdriver.Chrome(service=servico, options=chrome_options)


print("iniciando automação...")
navegador.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

# fazendo login
try:
    email_field = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    email_field.send_keys(os.getenv("LOGIN_EMAIL"))
    
    password_field = navegador.find_element(By.ID, "password")
    password_field.send_keys(os.getenv("LOGIN_SENHA"))
    
    botao_logar = navegador.find_element(By.ID, "pgtpy-botao")
    botao_logar.click()
    
    time.sleep(3)
    print("login realizado")

except (TimeoutException, NoSuchElementException) as e:
    print(f"erro no login: {e}")
    navegador.save_screenshot("screenshots/erro_login.png")
    navegador.quit()
    exit(1)


# cadastrando produtos
tabela = pd.read_csv("produtos.csv")
print(f"cadastrando {len(tabela)} produtos...")

for linha in tabela.index:
    try:
        # aguardando página de cadastro carregar
        campo_codigo = WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.ID, "codigo"))
        )
        campo_codigo.clear()
        campo_codigo.send_keys(tabela.loc[linha, "codigo"])
        
        # preenchendo campos
        navegador.find_element(By.ID, "marca").send_keys(tabela.loc[linha, "marca"])
        navegador.find_element(By.ID, "tipo").send_keys(tabela.loc[linha, "tipo"])
        navegador.find_element(By.ID, "categoria").send_keys(str(tabela.loc[linha, "categoria"]))
        navegador.find_element(By.ID, "preco_unitario").send_keys(str(tabela.loc[linha, "preco_unitario"]))
        navegador.find_element(By.ID, "custo").send_keys(str(tabela.loc[linha, "custo"]))
        
        obs = str(tabela.loc[linha, "obs"])
        if obs != "nan":
            navegador.find_element(By.ID, "obs").send_keys(obs)
        
        # enviando formulário
        botao_enviar = WebDriverWait(navegador, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'], .btn-primary, #pgtpy-botao"))
        )
        botao_enviar.click()
        time.sleep(1)
        
        if (linha + 1) % 10 == 0:
            print(f"{linha + 1} produtos cadastrados")
            
    except (TimeoutException, NoSuchElementException) as e:
        print(f"erro no produto {linha + 1}: {e}")
        navegador.save_screenshot(f"screenshots/erro_produto_{linha + 1}.png")
        break

print("cadastro finalizado")
navegador.quit()