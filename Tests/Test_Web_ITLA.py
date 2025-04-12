from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ITLAWebTest:

    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://itla.edu.do/")
        print("Página inicial cargada")

    def buscar(self):
        try:
            time.sleep(2)
            self.driver.save_screenshot("./Report/screenshots/Test_busqueda/Test_barra_busqueda.png")
            time.sleep(2)
            search = self.driver.find_element(By.ID, "search-form-1")
            search.send_keys("Desarrollo de Software")
            search.send_keys(Keys.RETURN)
            time.sleep(2)
            assert "Tecnología en Desarrollo de Software" in self.driver.page_source
            self.driver.save_screenshot("./Report/screenshots/Test_busqueda/Test_barra_busqueda_2.png")
            time.sleep(2)
            self.driver.back()
            time.sleep(2)
            print("\U00002705 Prueba de búsqueda")
        except Exception as e:
            print("\U0000274C Error en búsqueda:", e)

            

    def click_carreras(self):
        try:
            self.driver.save_screenshot("./Report/screenshots/Test_Carreras/Test_btn_carrera.png")
            btn = self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'a[aria-label*="Carreras Tecnológicas"]')))
            btn.click()
            time.sleep(2)
            self.driver.execute_script("window.scrollBy(0, 1000);")
            time.sleep(2)
            self.driver.execute_script("window.scrollBy(0, -1000);")
            assert "NUESTRAS CARRERAS" in self.driver.page_source
            self.driver.save_screenshot("./Report/screenshots/Test_Carreras/Test_btn_carrera_2.png")
            time.sleep(2)
            self.driver.back()
            time.sleep(5)
            print("\U00002705 Botón Carreras Tecnológicas")
        except Exception as e:
            print("\U0000274C Error en botón Carreras:", e)

    def volver_inicio(self):
        try:
            self.driver.get("https://itla.edu.do/")
            print("\U00002705 Página recargada")
        except Exception as e:
            print("\U0000274C Error al volver a la página principal:", e)


    def click_extensiones(self):
        try:
            self.driver.save_screenshot("./Report/screenshots/Test_Extensiones/Test_btn_Extenciones.png")
            btn = self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'a[aria-label*="Extensiones ITLA: Conocer más sobre nuestras extensiones."]')))
            
            btn.click()
            time.sleep(5)
            self.driver.execute_script("window.scrollBy(0, 700);")
            time.sleep(5)
            self.driver.execute_script("window.scrollBy(0, -700);")
            assert "Extensiones ITLA" in self.driver.page_source
            self.driver.save_screenshot("./Report/screenshots/Test_Extensiones/Test_btn_Extenciones_2.png")
            time.sleep(5)
            print("\U00002705 Botón Extensiones ITLA")
        except Exception as e:
            print("\U0000274C Error en botón Extensiones:", e)

    def test_navbar(self):
        botones = {
        "Inicio": '//li[@id="menu-item-16"]/a',
        "Sobre nosotros": '//li[@id="menu-item-864"]/a',
        "Servicios": '//li[@id="menu-item-865"]/a',
        "Transparencia": '//li[@id="menu-item-178"]/a',
        "Noticias": '//li[@id="menu-item-179"]/a',
        "Admisiones": '//li[@id="menu-item-885"]/a',
        "Emprendimiento": '//li[@id="menu-item-3031"]/a',
        "Portales en línea": '//li[@id="menu-item-4675"]/a',
    }

        for i, (nombre, xpath) in enumerate(botones.items(), start=1):
            try:
                btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
                btn.click()
                time.sleep(2)
                # Guardar screenshot con índice y nombre del botón limpio (sin espacios)
                nombre_archivo = f"./Report/screenshots/Test_navbar/{i}_{nombre.replace(' ', '_')}.png"
                self.driver.save_screenshot(nombre_archivo)
                print(f"\U00002705 Botón {nombre} (screenshot: {nombre_archivo})")
            except Exception as e:
                print(f"\U0000274C Error en botón {nombre}:", e)

    def test_chatbot(self):
        try:
            self.driver.save_screenshot("./Report/screenshots/Test_chatbot/Test_Chatbot.png")
            time.sleep(5)
            chat_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//summary[@class="svelte-1bweba"]')))
            chat_btn.click()
            self.driver.save_screenshot("./Report/screenshots/Test_chatbot/Test_Chatbot_open.png")
            chat_input = self.driver.find_element(By.XPATH, '//input[@class="svelte-42uc0m"]')
            chat_input.send_keys("Hola, esto es una prueba automatizada")
            chat_input.send_keys(Keys.RETURN)
            self.driver.save_screenshot("./Report/screenshots/Test_chatbot/Test_Chatbot_Message.png")
            time.sleep(2)
            assert "Instituto Tecnologico" in self.driver.page_source
            self.driver.save_screenshot("./Report/screenshots/Test_chatbot/Test_Chatbot_answer.png")
            time.sleep(5)
            print("\U00002705 Prueba Chatbot")
        except Exception as e:
            print("\U0000274C Error en chatbot:", e)

    

    def cerrar(self):
        time.sleep(5)
        self.driver.quit()
        print("Navegador cerrado")


# Ejecución de pruebas
