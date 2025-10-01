# Importa o módulo principal do Selenium para controlar o navegador
from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Forma correta no Selenium 4+
from selenium.webdriver.common.keys import Keys       # Teclas do teclado (ex: ENTER)
from selenium.webdriver.common.by import By           # ✅ Import necessário para localizar elementos
import time

print("Iniciando nosso robô...\n")

# Caminho do ChromeDriver
service = Service(r'C:\Users\Luigg\Desktop\Robos\chromedriver.exe')
driver = webdriver.Chrome(service=service)
# Abre o site
driver.get("https://registro.br/")

# ✅ Localiza a barra de pesquisa pelo ID
# No site registro.br, o campo tem id="is-avail-field"
pesquisa = driver.find_element(By.ID, "is-avail-field")
# Limpa o campo antes de digitar
pesquisa.clear()
# Digita o domínio desejado
pesquisa.send_keys("roboscompython.com.br")
# Pressiona ENTER para pesquisar
pesquisa.send_keys(Keys.RETURN)

resultados = driver.find_elements(By.TAG_NAME, "strong")
import pdb; pdb.set_trace()

time.sleep(8)
# Fecha o navegador
driver.close()