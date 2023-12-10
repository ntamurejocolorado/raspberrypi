import RPi.GPIO as GPIO
import time

# Configurar el modo GPIO
GPIO.setmode(GPIO.BCM)

# Pines GPIO para los colores del LED RGB
pin_rojo = 17
pin_verde = 27
pin_azul = 22

# Configurar los pines como salida
GPIO.setup(pin_rojo, GPIO.OUT)
GPIO.setup(pin_verde, GPIO.OUT)
GPIO.setup(pin_azul, GPIO.OUT)

try:
    # Encender y apagar cada color
    while True:
        # Encender el rojo
        GPIO.output(pin_rojo, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(pin_rojo, GPIO.LOW)

        # Encender el verde
        GPIO.output(pin_verde, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(pin_verde, GPIO.LOW)

        # Encender el azul
        GPIO.output(pin_azul, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(pin_azul, GPIO.LOW)

except KeyboardInterrupt:
    # Limpiar los recursos de GPIO al salir
    GPIO.cleanup()
