# Script de debug para testar a automação
import pandas
import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# carregando as variaveis de ambiente do arquivo .env
load_dotenv()

# configura as opcoes do chrome para rodar em modo Headless
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")

servico = ChromeService(executable_path='/usr/bin/chromedriver')
navegador = webdriver.Chrome(service=servico, options=chrome_options)

try:
    print("Navegador configurado em modo Headless. Iniciando a automação...")
    navegador.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
    
    # Aguarda a página carregar completamente
    time.sleep(3)
    
    print("Página carregada. Título:", navegador.title)
    print("URL atual:", navegador.current_url)
    
    # Salva screenshot para debug
    navegador.save_screenshot("debug_page_load.png")
    print("Screenshot salvo: debug_page_load.png")
    
    # Tenta encontrar elementos na página
    print("Procurando elementos na página...")
    
    # Verifica se há campos de login
    try:
        email_field = navegador.find_element(By.ID, "email")
        print("Campo de email encontrado!")
    except NoSuchElementException:
        print("Campo de email NÃO encontrado")
    
    try:
        password_field = navegador.find_element(By.ID, "senha")
        print("Campo de senha encontrado!")
    except NoSuchElementException:
        print("Campo de senha NÃO encontrado")
    
    # Procura por botões
    buttons = navegador.find_elements(By.TAG_NAME, "button")
    print(f"Encontrados {len(buttons)} botões na página")
    
    for i, button in enumerate(buttons):
        print(f"Botão {i+1}: texto='{button.text}', class='{button.get_attribute('class')}'")
    
    # Procura por links
    links = navegador.find_elements(By.TAG_NAME, "a")
    print(f"Encontrados {len(links)} links na página")
    
    # Salva o HTML da página para análise
    with open("debug_page_source.html", "w", encoding="utf-8") as f:
        f.write(navegador.page_source)
    print("HTML da página salvo: debug_page_source.html")
    
except Exception as e:
    print(f"Erro durante a execução: {e}")
    navegador.save_screenshot("debug_error.png")
    print("Screenshot de erro salvo: debug_error.png")

finally:
    navegador.quit()
    print("Navegador fechado.")