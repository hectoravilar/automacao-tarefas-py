# script de debug otimizado
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# configurando chrome headless
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

servico = ChromeService(executable_path='/usr/bin/chromedriver')
navegador = webdriver.Chrome(service=servico, options=chrome_options)

try:
    print("testando conexão com o site...")
    navegador.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
    time.sleep(2)
    
    # verificando elementos essenciais
    elementos_encontrados = []
    
    try:
        navegador.find_element(By.ID, "email")
        elementos_encontrados.append("email")
    except NoSuchElementException:
        pass
    
    try:
        navegador.find_element(By.ID, "password")
        elementos_encontrados.append("password")
    except NoSuchElementException:
        pass
    
    try:
        navegador.find_element(By.ID, "pgtpy-botao")
        elementos_encontrados.append("botão login")
    except NoSuchElementException:
        pass
    
    print(f"elementos encontrados: {elementos_encontrados}")
    
    # salvando screenshot apenas se necessário
    if len(elementos_encontrados) < 3:
        navegador.save_screenshot("screenshots/debug_page_load.png")
        print("screenshot salvo para análise")
    else:
        print("página carregou corretamente")
    
except Exception as e:
    print(f"erro: {e}")
    navegador.save_screenshot("screenshots/debug_error.png")

finally:
    navegador.quit()