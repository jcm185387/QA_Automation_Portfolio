import os
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

# Crear carpeta screenshots en la misma ruta del script
base_dir = os.path.join(os.path.dirname(__file__), "screenshots")
os.makedirs(base_dir, exist_ok=True)

# Subcarpeta con fecha y hora para cada ejecución
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
screenshot_dir = os.path.join(base_dir, f"run_{timestamp}")
os.makedirs(screenshot_dir, exist_ok=True)

print("Guardando screenshots en:", screenshot_dir)

def login(usuario, password):
    driver.get("https://www.saucedemo.com/")
    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    # Espera a que aparezca el carrito como señal de login exitoso
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_link")))
    driver.save_screenshot(os.path.join(screenshot_dir, "01_login.png"))

def agregar_producto():
    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))
    driver.save_screenshot(os.path.join(screenshot_dir, "02_carrito.png"))

def checkout(nombre, apellido, cp):
    driver.find_element(By.ID, "checkout").click()
    wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys(nombre)
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
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))
    driver.save_screenshot(os.path.join(screenshot_dir, "03_checkout.png"))

def finalizar_compra():
    wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()
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

driver.quit()
