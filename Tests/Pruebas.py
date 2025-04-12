from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

# Configuración inicial del WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

# Abre la página web del ITLA
try:
    driver.get("https://itla.edu.do/")
    print("\U00002705 Cargado de pagina")
    

except Exception as e:
    print("\U0000274C La prueba falló")




# Prueba para verificar la barra de búsqueda
try:
    
    search = driver.find_element(By.ID, "search-form-1")
    search.send_keys("Desarrollo de Software")  
    search.send_keys(Keys.RETURN)
    time.sleep(2) 
    print("\U00002705 Prueba de busqueda")

except Exception as e:
    print("\U0000274C Prueba de busqueda")

time.sleep(5)
wait = WebDriverWait(driver, 10)

driver.back()

time.sleep(3)
driver.execute_script("window.scrollBy(0, 200);")
time.sleep(2)


#Probar boton de carreras tecnologicas
try:
    wait = WebDriverWait(driver, 10)
    carreras_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[aria-label*="Carreras Tecnológicas"]')
))

    carreras_btn.click()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, -1000);")
    print("\U00002705 Boton carrera tecnologica")
except Exception as e:
    print("\U0000274C Boton carrera tecnologica:")

time.sleep(2)
driver.back()
time.sleep(2)

#Probar boton de Extensiones itla
try:
    wait = WebDriverWait(driver, 10)
    ext_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[aria-label*="Extensiones ITLA: Conocer más sobre nuestras extensiones."]')
))

    ext_btn.click()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 350);")
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, -350);")
    print("\U00002705 Boton carrera tecnologica")
except Exception as e:
    print("\U0000274C Boton carrera tecnologica:")


time.sleep(5)

#Probar botones del navbar

#test boton de inicio
try:
  
    wait = WebDriverWait(driver, 10)
    home_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//li[@id="menu-item-16"]/a')
))

    home_btn.click()
    time.sleep(2)
    print("\U00002705 boton de inicio")
except Exception as e:
    print("\U0000274C boton de inicio:", e)

time.sleep(2)

#test boton "Sobre nosotros"
try:
   
    wait = WebDriverWait(driver, 10)
    about_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//li[@id="menu-item-864"]/a')
))
    

    about_btn.click()
    time.sleep(2)
    print("\U00002705 Sobre nosotros")
except Exception as e:
    print("\U0000274C Sobre nosotros:", e)


#test boton "servicios"
try:
   
    wait = WebDriverWait(driver, 10)
    Serv_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//li[@id="menu-item-865"]/a')
))
    

    Serv_btn.click()
    time.sleep(2)
    print("\U00002705 boton servicios")
except Exception as e:
    print("\U0000274C boton servicios:", e)    

#test boton "trasparencia"
try:
   
    wait = WebDriverWait(driver, 10)
    transp_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//li[@id="menu-item-178"]/a')
))
    

    transp_btn.click()
    time.sleep(2)
    print("\U00002705 boton servicios")
except Exception as e:
    print("\U0000274C boton servicios:", e)


#test boton "noticias"
try:
   
    wait = WebDriverWait(driver, 10)
    News_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//li[@id="menu-item-179"]/a')
))
    

    News_btn.click()
    time.sleep(2)
    print("\U00002705 boton noticias")
except Exception as e:
    print("\U0000274C boton noticia", e)            
    

#test boton "Admisiones"
try:
   
    wait = WebDriverWait(driver, 10)
    Admis_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//li[@id="menu-item-885"]/a')
))
    

    Admis_btn.click()
    time.sleep(2)
    print("\U00002705 boton Admisiones")
except Exception as e:
    print("\U0000274C boton Admisiones", e)            
    

#test boton "Emprendimiento"
try:
   
    wait = WebDriverWait(driver, 10)
    Emp_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//li[@id="menu-item-3031"]/a')
))
    

    Emp_btn.click()
    time.sleep(2)
    print("\U00002705 boton Emprendimiento")
except Exception as e:
    print("\U0000274C boton Emprendimiento", e)            
    

#test boton "portales en linea"
try:
   
    wait = WebDriverWait(driver, 10)
    Portal_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//li[@id="menu-item-4675"]/a')
))
    

    Portal_btn.click()
    time.sleep(2)
    print("\U00002705 boton portales en linea")
except Exception as e:
    print("\U0000274C boton portales en linea", e)            

time.sleep(2)


#test boton e input del chatbot
try:
   
    wait = WebDriverWait(driver, 10)
    chat_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//summary[@class="svelte-1bweba"]')
))
    

    chat_btn.click()
    Chat_input = driver.find_element(By.XPATH, '//input[@class="svelte-42uc0m"]')
    Chat_input.send_keys("Hola, esto es una prueba automatizada")  
    Chat_input.send_keys(Keys.RETURN)
    time.sleep(2) 


    time.sleep(2)
    print("\U00002705 boton portales en linea")
except Exception as e:
    print("\U0000274C boton portales en linea", e)  


#regresar a la pagina principal
try:
    driver.get("https://itla.edu.do/")
    print("\U00002705 Cargado de pagina")
    

except Exception as e:
    print("\U0000274C Cargado de pagina", e)


time.sleep(10)
# Cierra el navegador después de la prueba
driver.quit()
