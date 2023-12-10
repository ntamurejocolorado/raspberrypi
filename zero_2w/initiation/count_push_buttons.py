from functools import partial
from pydantic import BaseModel
from typing import Callable, Any
import RPi.GPIO as GPIO
import time
import logging

    
def button_callback(channel,button):
    button.pulses += 1
    logging.info(f'Channel: {channel}, Title: {button.title_for_event}, Pulsado: {button.pulses} veces')

def configure_gpio_input(input: int):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(input, GPIO.IN)
        
def configure_event(input:int, event, callback):
    GPIO.add_event_detect(input, event, callback, bouncetime=200)
        
def configuration_buttons(lst_buttons):
    for button in lst_buttons:
        configure_gpio_input(input=button.number_input)
        callback_with_title = partial(button.callback, button=button)
        configure_event(input=button.number_input, event=button.event_to_use, callback=callback_with_title)
        
def run():
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Exception")
        pass
    finally:
        GPIO.cleanup()
        
class GPIOPARAMS(BaseModel):
    number_input: int
    event_to_use: Any
    title_for_event: str = "sample to show in logging"
    callback: Callable
    pulses: int
    
def main():
    logging.basicConfig(encoding='utf-8', level=logging.INFO)
    logging.info("Hello Raspberry Zero: Count push buttons")
    
    button_1 = GPIOPARAMS(number_input=2,event_to_use=GPIO.FALLING,title_for_event="Pushed button in GPIO 2",callback=button_callback, pulses=0)
    #button_2 = GPIOPARAMS(number_input=3,event_to_use=GPIO.FALLING,title_for_event="Pushed button in GPIO 3",callback=button_callback, pulses=0)
    
    configuration_buttons(lst_buttons=[button_1])

    
    run()

if __name__ == "__main__":
    main()
