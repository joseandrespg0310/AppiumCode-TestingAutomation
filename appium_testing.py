from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep

options = UiAutomator2Options()
options.platform_name = "Android"
options.platform_version = "15"  # Cambiado a la versión obtenida
options.device_name = "sdk_gphone64_x86_64"  # Cambiado al modelo obtenido
options.app_package = "com.example.chocopop"
options.app_activity = "com.example.chocopop.MainActivity"
options.automation_name = "UiAutomator2"

# Conexión única al servidor Appium
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)


try:
    # Prueba 1: Click en el Boton sin Ingresar Credenciales

    sleep(3)
    login_button = driver.find_element(AppiumBy.ID, "com.example.chocopop:id/login_iniciar_sesion")
    login_button.click()
    print("Se hizo clic en el botón de iniciar sesión sin credenciales.")

    # Prueba 2: Usuario y Contraseñas Invalidos

    sleep(3)
    login_usuario_error = driver.find_element(AppiumBy.ID, "com.example.chocopop:id/login_usuario")
    login_usuario_error.send_keys("Juan")
    print("Se escribió un usuario que no existe.")

    login_contraseña_error = driver.find_element(AppiumBy.ID, "com.example.chocopop:id/login_contraseña")
    login_contraseña_error.send_keys("Error")
    print("Se escribió una contraseña inválida.")

    login_button_error = driver.find_element(AppiumBy.ID, "com.example.chocopop:id/login_iniciar_sesion")
    login_button_error.click()
    print("Se hizo clic en el botón de iniciar sesión con credenciales inválidas.")

    # Prueba 3: Usuario y Contraseña Válidos

    sleep(3)
    login_usuario = driver.find_element(AppiumBy.ID, "com.example.chocopop:id/login_usuario")
    login_usuario.clear()  
    login_usuario.send_keys("Choco")
    print("Se escribió 'Choco' en el campo de usuario.")

    login_contraseña = driver.find_element(AppiumBy.ID, "com.example.chocopop:id/login_contraseña")
    login_contraseña.clear()  
    login_contraseña.send_keys("ChocoPop2026")
    print("Se escribió 'ChocoPop2026' en el campo de contraseña.")

    login_button = driver.find_element(AppiumBy.ID, "com.example.chocopop:id/login_iniciar_sesion")
    login_button.click()
    print("Se hizo clic en el botón de iniciar sesión con credenciales válidas.")

    sleep(7)

except Exception as e:
    print(f"Hubo un error: {e}")

finally:
  
    driver.quit()


# AHORA PARA EL APARTADO DE REGISTRO

# Conexión única al servidor Appium

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
try:
    # Espera para asegurar que la pantalla se haya cargado
    sleep(3)

    # Paso 1: Haz clic en el botón para ir a la sección de registro
    register_prompt = driver.find_element(AppiumBy.ID, "com.example.chocopop:id/login_register_prompt")
    register_prompt.click()
    print("Se hizo clic en el botón de registro.")

    # Espera para que se cargue la pantalla de registro
    sleep(3)

    # Paso 2: Completar los campos del formulario de registro
    register_nombre = driver.find_element(AppiumBy.ID, "com.example.chocopop:id/register_nombre")
    register_nombre.send_keys("Prueba1")
    print("Se escribió 'Prueba1' en el campo de nombre.")

    register_correo = driver.find_element(AppiumBy.ID, "com.example.chocopop:id/register_correo")
    register_correo.send_keys("Prueba1")
    print("Se escribió 'Prueba1' en el campo de correo.")

    register_contraseña = driver.find_element(AppiumBy.ID, "com.example.chocopop:id/register_contraseña")
    register_contraseña.send_keys("Prueba1")
    print("Se escribió 'Prueba1' en el campo de contraseña.")

    register_telefono = driver.find_element(AppiumBy.ID, "com.example.chocopop:id/register_telefono")
    register_telefono.send_keys("123")
    print("Se escribió '123' en el campo de teléfono.")

    register_direccion = driver.find_element(AppiumBy.ID, "com.example.chocopop:id/register_direccion")
    register_direccion.send_keys("defecto")
    print("Se escribió 'defecto' en el campo de dirección.")

    # Paso 3: botón para confirmar el registro, agrégalo aquí
   
    register_button = driver.find_element(AppiumBy.ID, "com.example.chocopop:id/register_button")
    register_button.click()
    print("Se hizo clic en el botón de confirmar registro.")

    sleep(8)

except Exception as e:
    print(f"Hubo un error durante el registro: {e}")

finally:
    # Finaliza la sesión
    driver.quit()
