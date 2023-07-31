from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import pandas as pd
import os 
import sys

aplicacion_ruta = os.path.dirname(sys.executable)

# Programar un día y hora para ejecutar el script
now = datetime.now()
mes_dia_ano = now.strftime("%m%d%Y") #mmddYYYY

website = "https://www.cotodigital3.com.ar/sitios/cdigi/browse/ofertas-todas-las-ofertas/_/N-c7ha3p"
path = "C:/Users/Virgi/Desktop/Virginia/Programacion/WebServer Chrome/chromedriver"

# Headless mode
options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

conteiners = driver.find_elements(by="xpath", value="//div[@class='product_info_container']")

productos = []
precios_unitarios = []
links_ofertas = []

for conteiner in conteiners:
    producto=conteiner.find_element(by="xpath", value="./a/span[@class='atg_store_productTitle']/div/span/div").text
    precio_unitario=conteiner.find_element(by="xpath", value="./span[@class='unit']").text
    link_oferta=conteiner.find_element(by="xpath", value="./a").get_attribute("href")                               
    productos.append(producto)
    precios_unitarios.append(precio_unitario)
    links_ofertas.append(link_oferta)

driver.quit()

mi_diccionario = {'producto': productos,'precio_unitario': precios_unitarios, 'link_oferta': links_ofertas}

df_ofertas = pd.DataFrame(mi_diccionario)

nombre_archivo = f'ofertas_coto_{mes_dia_ano}.csv'
path_final = os.path.join(aplicacion_ruta, nombre_archivo)
df_ofertas.to_csv(path_final)




