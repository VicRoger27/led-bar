i = 0
led.enable(False)
my_pins = [DigitalPin.P0,
    DigitalPin.P1,
    DigitalPin.P2,
    DigitalPin.P3,
    DigitalPin.P4,
    DigitalPin.P10,
    DigitalPin.P6,
    DigitalPin.P7,
    DigitalPin.P9,
    DigitalPin.P8]

def on_forever():
    global i
    i = len(my_pins) - 1
    while i >= 0:
        p = my_pins[i]
        pins.digital_write_pin(p, 1)
        pause(100)
        pins.digital_write_pin(p, 0)
        i += 0 - 1
basic.forever(on_forever)
