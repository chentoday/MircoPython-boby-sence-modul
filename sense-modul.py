from machine import Pin

led = Pin(18, Pin.OUT)
p5 = Pin(35, Pin.IN)
p5.value(0)
while 1:
    if (p5.value() == 1):
        led.value(1)
    else:
        led.value(0)
