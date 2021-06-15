#Librerias
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as expect
import requests


# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = '.\chromedriver.exe'

driver = webdriver.Chrome(driver_path, chrome_options=options)

# Inicializamos el navegador
driver.get('https://es.quora.com')

# Loguearse
login = '#root > div:nth-child(2) > div > div > div > div > div > div.q-flex.qu-mb--large > div:nth-child(2) > div.q-flex.qu-justifyContent--space-between.qu-alignItems--center > button'

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#email')))\
    .send_keys('valerisvso@gmail.com')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#password')))\
    .send_keys('Coronavirus2020')

driver.find_element_by_css_selector(login).click()

# Entrar en el perfil del usuario

driver.get('https://es.quora.com/profile/Omar-Bessa/answers')
respuesta = driver.find_elements_by_xpath('//span[@class="q-box"]')

# Seleccionar opcion respuestas
cuerpo_de_texto = driver.find_elements_by_class_name('q-box')
for texto in cuerpo_de_texto:
    print(texto.text)
    
time.sleep(7)

driver.quit()