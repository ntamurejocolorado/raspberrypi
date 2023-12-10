from functools import partial
from pydantic import BaseModel
from typing import Callable, Any
import RPi.GPIO as GPIO
import time
import logging

            
def run():
    
    GPIO.setmode(GPIO.BCM)
    buzzer_pin = 17
    GPIO.setup(buzzer_pin, GPIO.OUT)
    try:
        while True:
            logging.info("Buzzer ON")
            buzzer = GPIO.PWM(buzzer_pin, 440)  # 440 Hz es un tono típico
            buzzer.start(50)  # Iniciar PWM al 50% de ciclo de trabajo
            time.sleep(5)
            logging.info("Buzzer OFF")
            buzzer.stop()
            time.sleep(2)
            
    except KeyboardInterrupt:
        logging.info("Exception")
        pass
    finally:
        GPIO.cleanup()
        
    
def main():
    logging.basicConfig(encoding='utf-8', level=logging.INFO)
    logging.info("Hello Raspberry Zero: Passive Buzzer")
    run()

if __name__ == "__main__":
    main()
