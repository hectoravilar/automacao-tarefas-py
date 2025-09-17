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
# usando WebDriverWait para esperar ate 10 segundos para o campo aparecer.
try:
    print("Procurando o botão de login e aguardando ficar clicável...")
    botao_logar = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-primary"))
    )
    botao_logar.click()
    print("Botão de login clicado com sucesso.")

except TimeoutException:
    # se der um erro de timeout, tira um print e avisa
    print("ERRO: O botão de login não ficou clicável em 10 segundos.")
    navegador.save_screenshot("screenshot_erro.png")
    print("Screenshot 'screenshot_erro.png' salvo para análise.")
    # para o script para não continuar com o erro
    raise


# importando base de dados e cadastrando os produtos
tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    # usando um Wait aqui no primeiro campo do loop para garantir que a página carregou.
    campo_codigo = WebDriverWait(navegador, 10).until(
        EC.presence_of_element_located((By.ID, "codigo"))
    )
    campo_codigo.send_keys(tabela.loc[linha, "codigo"])


    navegador.find_element(By.ID, "marca").send_keys(tabela.loc[linha, "marca"])
    navegador.find_element(By.ID, "tipo").send_keys(tabela.loc[linha, "tipo"])
    navegador.find_element(By.ID, "categoria").send_keys(str(tabela.loc[linha, "categoria"]))
    navegador.find_element(By.ID, "preco_unitario").send_keys(str(tabela.loc[linha, "preco_unitario"]))
    navegador.find_element(By.ID, "custo").send_keys(str(tabela.loc[linha, "custo"]))


    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        navegador.find_element(By.ID, "obs").send_keys(obs)

    # clicando no botao de enviar
    navegador.find_element(By.CLASS_NAME, "btn-primary").click()


time.sleep(5) # uma pausa pra ver a ultima tela antes de fechar
navegador.quit() # fecha o navegador e encerra o processo do chromedriver