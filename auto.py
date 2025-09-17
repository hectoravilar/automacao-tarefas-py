# importando bibliotecas
import pandas
import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException


# carregando as variaveis de ambiente do arquivo .env
load_dotenv()

# configura as opcoes do chrome para rodar em modo Headless
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")

servico = ChromeService(executable_path='/usr/bin/chromedriver')
navegador = webdriver.Chrome(service=servico, options=chrome_options)


print("Navegador configurado em modo Headless. Iniciando a automação...")
navegador.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login")


# fazendo Login
# preenchendo os campos de email e senha
try:
    print("Preenchendo campos de login...")
    
    # preenchendo o email
    email_field = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    email_field.send_keys(os.getenv("LOGIN_EMAIL"))
    print("Email preenchido.")
    
    # preenchendo  a senha
    password_field = navegador.find_element(By.ID, "password")
    password_field.send_keys(os.getenv("LOGIN_SENHA"))
    print("Senha preenchida.")
    
    # clicando no botão de login
    botao_logar = navegador.find_element(By.ID, "pgtpy-botao")
    botao_logar.click()
    print("Botão de login clicado com sucesso.")
    
    # aguardando a pagina de cadastro carregar
    time.sleep(3)
    print("Aguardando redirecionamento para página de cadastro...")

except TimeoutException:
    print("ERRO: Elementos de login não encontrados.")
    navegador.save_screenshot("screenshot_erro.png")
    print("Screenshot 'screenshot_erro.png' salvo para análise.")
    raise
except Exception as e:
    print(f"ERRO durante o login: {e}")
    navegador.save_screenshot("screenshot_erro.png")
    print("Screenshot 'screenshot_erro.png' salvo para análise.")
    raise


# importando base de dados e cadastrando os produtos
tabela = pandas.read_csv("produtos.csv")
print(f"Iniciando cadastro de {len(tabela)} produtos...")

for linha in tabela.index:
    print(f"Cadastrando produto {linha + 1}/{len(tabela)}: {tabela.loc[linha, 'codigo']}")
    
    # usando um Wait aqui no primeiro campo do loop para garantir que a página carregou.
    try:
        campo_codigo = WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.ID, "codigo"))
        )
        campo_codigo.clear()  # Limpa o campo antes de preencher
        campo_codigo.send_keys(tabela.loc[linha, "codigo"])
    except TimeoutException:
        print(f"Erro: Campo código não encontrado para produto {linha + 1}")
        navegador.save_screenshot(f"erro_campo_codigo_{linha + 1}.png")
        break

    navegador.find_element(By.ID, "marca").send_keys(tabela.loc[linha, "marca"])
    navegador.find_element(By.ID, "tipo").send_keys(tabela.loc[linha, "tipo"])
    navegador.find_element(By.ID, "categoria").send_keys(str(tabela.loc[linha, "categoria"]))
    navegador.find_element(By.ID, "preco_unitario").send_keys(str(tabela.loc[linha, "preco_unitario"]))
    navegador.find_element(By.ID, "custo").send_keys(str(tabela.loc[linha, "custo"]))

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        navegador.find_element(By.ID, "obs").send_keys(obs)

    # clicando no botao de enviar
    try:
        
        botao_enviar = WebDriverWait(navegador, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit'], .btn-primary, #pgtpy-botao"))
        )
        botao_enviar.click()
        print(f"Produto {linha + 1} cadastrado com sucesso.")
        time.sleep(1)  # Pausa entre cadastros
    except TimeoutException:
        print(f"Erro ao encontrar botão de envio para produto {linha + 1}")
        navegador.save_screenshot(f"erro_produto_{linha + 1}.png")
        break


time.sleep(5) # uma pausa pra ver a ultima tela antes de fechar
navegador.quit() # fecha o navegador e encerra o processo do chromedriver