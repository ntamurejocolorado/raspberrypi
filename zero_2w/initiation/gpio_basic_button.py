import RPi.GPIO as GPIO
import time

def button_callback(channel):
    print('Has pulsado el boton')

def main():
    print("Hello Raspberry Zero")

    # Configurar el modo GPIO
    GPIO.setmode(GPIO.BCM)

    # Configurar el pin GPIO 2 como entrada
    GPIO.setup(2, GPIO.IN)

    # Configurar un evento para detectar cuando el botón es presionado
    GPIO.add_event_detect(2, GPIO.FALLING, callback=button_callback, bouncetime=200)

    # Mantener el programa en ejecución para poder detectar el evento del botón
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Limpiar los recursos de GPIO al salir
        GPIO.cleanup()

if __name__ == "__main__":
    main()
