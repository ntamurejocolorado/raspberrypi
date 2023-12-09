import RPi.GPIO as GPIO
import time

def main():
    print("Hello Raspberry Zero")
    GPIO.setmode(GPIO.BCM)  # Use el número de pin BCM
    GPIO.setwarnings(False)

    onboardLED = 25
    GPIO.setup(onboardLED, GPIO.OUT)

    GPIO.output(onboardLED, GPIO.HIGH)  # Enciende el LED
    time.sleep(5)
    print("apagando...")
    GPIO.output(onboardLED, GPIO.LOW)


    
if __name__ == "__main__":
    main()