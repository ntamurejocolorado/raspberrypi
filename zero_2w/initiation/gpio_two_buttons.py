from functools import partial
import RPi.GPIO as GPIO
import time
import logging

    
def button_callback(channel,title):
    logging.info(title)

def configure_gpio(input: int):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(input, GPIO.IN)
        
def configure_events(input:int, event, callback):
    GPIO.add_event_detect(input, event, callback, bouncetime=200)

def run():
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Exception")
        pass
    finally:
        GPIO.cleanup()
        
class GPIOPARAMS():
    def __init__(self,number_input=0,event_to_use=None,title_for_event="sample",callback=None):
        self.number_input = number_input
        self.event_to_use = event_to_use
        self.title_for_event = str(title_for_event)
        self.callback = callback
    
def main():
    logging.basicConfig(encoding='utf-8', level=logging.INFO)
    logging.info("Hello Raspberry Zero")
    
    button_1 = GPIOPARAMS(number_input=2,event_to_use=GPIO.FALLING,title_for_event="Pulsado boton 1",callback=button_callback)
    button_2 = GPIOPARAMS(number_input=3,event_to_use=GPIO.FALLING,title_for_event="Pulsado boton 2",callback=button_callback)

    configure_gpio(input=button_1.number_input)
    callback_with_title = partial(button_1.callback, title=button_1.title_for_event)
    configure_events(input=button_1.number_input, event=button_1.event_to_use, callback=callback_with_title)
    
    configure_gpio(input=button_2.number_input)
    callback_with_title = partial(button_2.callback, title=button_2.title_for_event)
    configure_events(input=button_2.number_input, event=button_2.event_to_use, callback=callback_with_title)
    
    run()

if __name__ == "__main__":
    main()
