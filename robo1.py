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

dominios = ["roboscompython.com.br" , "udemy.com" , "uol.com.br" , "pythoncurso.com"] #vai pesquisar uma lista
for dominio in dominios:
    # ✅ Localiza a barra de pesquisa pelo ID
    # No site registro.br, o campo tem id="is-avail-field"
    pesquisa = driver.find_element(By.ID, "is-avail-field")
    pesquisa.clear() # Limpa o campo antes de digitar# ✅ Localiza a barra de pesquisa pelo ID
    # No site registro.br, o campo tem id="is-avail-field"
    pesquisa = driver.find_element(By.ID, "is-avail-field")
    pesquisa.clear() # Limpa o campo antes de digitar
    pesquisa.send_keys(dominio) # Digita o domínio desejado
    pesquisa.send_keys(Keys.RETURN) # Pressiona ENTER para pesquisar
    time.sleep(2)
    resultados = driver.find_elements(By.TAG_NAME, "strong")
    print("Domínio %s %s" % (dominio, resultados[2].text))

time.sleep(3)
driver.close() # Fecha o navegador