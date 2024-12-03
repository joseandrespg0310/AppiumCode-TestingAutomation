from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def iniciar_app():
    # Configuración inicial para la primera actividad (MainActivity)
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.platform_version = "15"
    options.device_name = "sdk_gphone64_x86_64"
    options.app_package = "com.example.chocopop"
    options.app_activity = "com.example.chocopop.MainActivity"
    options.automation_name = "UiAutomator2"

    # Conexión al servidor de Appium
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)

    # Esperar unos segundos para que cargue el Activity principal
    sleep(3)

    # Ingreso de credenciales
    login_usuario = driver.find_element(AppiumBy.ID, "com.example.chocopop:id/login_usuario")
    login_usuario.clear()  
    login_usuario.send_keys("Choco")
    print("Se escribió 'Choco' en el campo de usuario.")

    login_contraseña = driver.find_element(AppiumBy.ID, "com.example.chocopop:id/login_contraseña")
    login_contraseña.clear()  
    login_contraseña.send_keys("ChocoPop2026")
    print("Se escribió 'ChocoPop2026' en el campo de contraseña.")

    # Hacer clic en el botón de inicio de sesión
    login_button = driver.find_element(AppiumBy.ID, "com.example.chocopop:id/login_iniciar_sesion")
    login_button.click()
    print("Se hizo clic en el botón de iniciar sesión con credenciales válidas.")

    # Esperar unos segundos para que cargue el siguiente Activity
    sleep(3)

    # Esperar hasta que DashBoardActivity esté activo
    driver.wait_activity("com.example.chocopop.DashBoardActivity", 10)
    print("Se cambió a DashBoardActivity.")

    return driver
sleep(6)

# Llamamos a la función para iniciar la aplicación
driver = iniciar_app()

# Esperar hasta que el botón 'button_grid' esté disponible en DashBoardActivity
try:
    grid_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ID, "com.example.chocopop:id/button_grid"))
    )
    grid_button.click()
    print("Se hizo clic en el botón 'button_grid'.")
except Exception as e:
    print("Error al encontrar el botón 'button_grid':", str(e))
    sleep(5)

# Esperar hasta que el botón 'moreInfoButton' esté disponible y hacer clic en él
try:
    more_info_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ID, "com.example.chocopop:id/moreInfoButton"))
    )
    more_info_button.click()
    print("Se hizo clic en el botón 'moreInfoButton'.")
except Exception as e:
    print("Error al encontrar el botón 'moreInfoButton':", str(e))
sleep(4)


# Esperar hasta que el botón 'addToCartButton' esté disponible y hacer clic en él
try:
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ID, "com.example.chocopop:id/addToCartButton"))
    )
    add_to_cart_button.click()
    print("Se hizo clic en el botón 'addToCartButton'.")
except Exception as e:
    print("Error al encontrar el botón 'addToCartButton':", str(e))

# Esperamos un poco antes de cerrar la sesión
sleep(5)


# Cerrar la sesión de Appium al finalizar el primer test
driver.quit()

# Reabrir la aplicación y realizar las mismas acciones de nuevo
driver = iniciar_app()

# Esperar hasta que el botón 'button_info' esté disponible
try:
    info_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ID, "com.example.chocopop:id/button_info"))
    )
    info_button.click()
    print("Se hizo clic en el botón 'button_info'.")
except Exception as e:
    print("Error al encontrar el botón 'button_info':", str(e))

# Esperamos un poco antes de interactuar con 'button_phone'
sleep(2)

# Cerrar la sesión de Appium al finalizar el primer test
driver.quit()

# Reabrir la aplicación y realizar las mismas acciones de nuevo
driver = iniciar_app()

# Volver a obtener el botón 'button_phone' después de la interacción con 'button_info'
try:
    phone_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((AppiumBy.ID, "com.example.chocopop:id/button_phone"))
    )
    phone_button.click()
    print("Se hizo clic en el botón 'button_phone'.")
except Exception as e:
    print("Error al encontrar el botón 'button_phone':", str(e))

# Esperamos un poco antes de interactuar con 'btn_carrito'
sleep(5)
# Cerrar la sesión de Appium al finalizar el primer test
driver.quit()

# Reabrir la aplicación y realizar las mismas acciones de nuevo
driver = iniciar_app()

# Esperar hasta que el botón 'btn_carrito' esté disponible
try:
    carrito_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ID, "com.example.chocopop:id/btn_carrito"))
    )
    carrito_button.click()
    print("Se hizo clic en el botón 'btn_carrito'.")
except Exception as e:
    print("Error al encontrar el botón 'btn_carrito':", str(e))

# Esperar hasta que el botón 'increaseButton' esté disponible y hacer clic 11 veces
try:
    increase_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ID, "com.example.chocopop:id/increaseButton"))
    )

    # Hacer clic 11 veces en el botón 'increaseButton'
    for i in range(15):
        increase_button.click()
        print(f"Se hizo clic {i + 1} en el botón 'increaseButton'.")

except Exception as e:
    print("Error al encontrar el botón 'increaseButton':", str(e))

# Esperar hasta que el botón 'btn_comprar' esté disponible y hacer clic en él
try:
    comprar_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ID, "com.example.chocopop:id/btn_comprar"))
    )
    comprar_button.click()
    print("Se hizo clic en el botón 'btn_comprar'.")
except Exception as e:
    print("Error al encontrar el botón 'btn_comprar':", str(e))

# Cerrar la sesión de Appium al finalizar el segundo test
sleep(5)
driver.quit()


# Reabrir la aplicación y realizar las mismas acciones de nuevo
driver = iniciar_app()

# Esperar hasta que el botón 'btn_carrito' esté disponible
try:
    carrito_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ID, "com.example.chocopop:id/btn_carrito"))
    )
    carrito_button.click()
    print("Se hizo clic en el botón 'btn_carrito'.")
except Exception as e:
    print("Error al encontrar el botón 'btn_carrito':", str(e))

# Esperar hasta que el botón 'increaseButton' esté disponible y hacer clic 10 veces
try:
    increase_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ID, "com.example.chocopop:id/increaseButton"))
    )

    # Hacer clic 10 veces en el botón 'increaseButton'
    for i in range(10):
        increase_button.click()
        print(f"Se hizo clic {i + 1} en el botón 'increaseButton'.")

except Exception as e:
    print("Error al encontrar el botón 'increaseButton':", str(e))

# Esperar hasta que el botón 'decreaseButton' esté disponible y hacer clic 14 veces
try:
    decrease_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ID, "com.example.chocopop:id/decreaseButton"))
    )

    # Hacer clic 14 veces en el botón 'decreaseButton'
    for i in range(20):
        decrease_button.click()
        print(f"Se hizo clic {i + 1} en el botón 'decreaseButton'.")

except Exception as e:
    print("Error al encontrar el botón 'decreaseButton':", str(e))

# Esperar hasta que el botón 'btn_comprar' esté disponible y hacer clic en él


# Cerrar la sesión de Appium al finalizar el segundo test
sleep(5)
driver.quit()
