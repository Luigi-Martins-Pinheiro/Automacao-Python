# Importa o módulo principal do Selenium para controlar o navegador
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Forma correta no Selenium 4+
from selenium.webdriver.common.keys import Keys       # Teclas do teclado (ex: ENTER)
from selenium.webdriver.common.by import By           # ✅ Import necessário para localizar elementos
import time

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Remove mensagens extras do Chrome

print("Iniciando nosso robô...\n")

# Caminho do ChromeDriver
service = Service(r'C:\Users\Luigg\Desktop\Robos\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)
# Abre o site
driver.get("https://registro.br/")

# ✅ Localiza a barra de pesquisa pelo ID
# No site registro.br, o campo tem id="is-avail-field"
pesquisa = driver.find_element(By.ID, "is-avail-field")
# Limpa o campo antes de digitar
pesquisa.clear()
dominio = "roboscompython.com.br"
# Digita o domínio desejado
pesquisa.send_keys(dominio)
# Pressiona ENTER para pesquisar
pesquisa.send_keys(Keys.RETURN)
time.sleep(2)

resultados = driver.find_elements(By.TAG_NAME, "strong")
print("Domínio %s %s" % (dominio, resultados[2].text))

time.sleep(8)
# Fecha o navegador
driver.close()