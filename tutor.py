#!/usr/bin/python
from pyA20.gpio import gpio
from pyA20.gpio import port
from time import sleep
import random
import atexit

def exit_handler():
    for port in pairs:
        gpio.output(port[0], gpio.LOW)

atexit.register(exit_handler)

gpio.init()
relay1 = port.PA12
gpio.setcfg(relay1, gpio.OUTPUT)

relay2 = port.PA11
gpio.setcfg(relay2, gpio.OUTPUT)

relay3 = port.PA6
gpio.setcfg(relay3, gpio.OUTPUT)

relay = [relay1,relay2,relay3]

vib1 = port.PA13
gpio.setcfg(vib1, gpio.INPUT)

vib2 = port.PA1
gpio.setcfg(vib2, gpio.INPUT)

vib3 = port.PA0
gpio.setcfg(vib3, gpio.INPUT)

vib = [vib1,vib2,vib3]

pairs = [[relay[i], vib[i]] for i in range(len(vib))]

current = random.choice(pairs)

gpio.output(current[0], gpio.HIGH)
new = current
while True:
    result = gpio.input(current[1])
    if result != 1:
        while new == current:
            new = random.choice(pairs)

        print("vibrated")
        print(gpio.input(current[0]))
        gpio.output(current[0], gpio.LOW)
        gpio.output(new[0],gpio.HIGH)
        sleep(2)
        current = new

