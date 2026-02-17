import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

# Configuración de Chrome en modo incógnito
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

# Crear carpeta screenshots si no existe
base_dir = "Proyecto2_Ecommerce_Selenium/screenshots"
os.makedirs(base_dir, exist_ok=True)

# Subcarpeta con fecha y hora para cada ejecución
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
screenshot_dir = os.path.join(base_dir, f"run_{timestamp}")
os.makedirs(screenshot_dir, exist_ok=True)

def login(usuario, password):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    driver.save_screenshot(os.path.join(screenshot_dir, "01_login.png"))

def agregar_producto():
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.save_screenshot(os.path.join(screenshot_dir, "02_carrito.png"))

def checkout(nombre, apellido, cp):
    driver.find_element(By.ID, "checkout").click()
    first_name_field = wait.until(EC.presence_of_element_located((By.ID, "first-name")))
    first_name_field.send_keys(nombre)
    driver.find_element(By.ID, "last-name").send_keys(apellido)
    driver.find_element(By.ID, "postal-code").send_keys(cp)

    # Manejo de popup si apareciera
    try:
        alert = driver.switch_to.alert
        print("Popup detectado en checkout:", alert.text)
        alert.accept()
        print("Popup cerrado ✅")
    except NoAlertPresentException:
        print("No apareció popup en checkout, continuando...")

    driver.find_element(By.ID, "continue").click()
    driver.save_screenshot(os.path.join(screenshot_dir, "03_checkout.png"))

def finalizar_compra():
    finish_button = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
    finish_button.click()
    success_message = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
    ).text
    driver.save_screenshot(os.path.join(screenshot_dir, "04_confirmacion.png"))
    print("Texto capturado:", success_message)
    assert "thank you for your order" in success_message.lower()
    print("Flujo de compra automatizado exitoso ✅")

# Ejecución del flujo completo
login("standard_user", "secret_sauce")
agregar_producto()
checkout("Juan", "QA", "64000")
finalizar_compra()

# Espera de 3 segundos antes de cerrar
time.sleep(3)
driver.quit()
