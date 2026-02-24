
### `test_login.py`

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.options import Options

#se comenta pues se usará el chrome sin interfaz
# driver = webdriver.Chrome()

#Se agrega sección, para PIPELINES, al no haber interfaz gráfica en GITHUB ACTIONS se agregan opciones al navegador


options = Options()
options.add_argument("--headless")  # modo sin interfaz
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)




driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button.radius").click()

success_message = driver.find_element(By.ID, "flash").text
assert "You logged into a secure area!" in success_message

print("Prueba de login exitosa ✅")
time.sleep(3)
driver.quit()
