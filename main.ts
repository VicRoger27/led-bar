let i = 0
led.enable(false)
let my_pins = [
DigitalPin.P0,
DigitalPin.P1,
DigitalPin.P2,
DigitalPin.P3,
DigitalPin.P4,
DigitalPin.P10,
DigitalPin.P6,
DigitalPin.P7,
DigitalPin.P9,
DigitalPin.P8
]
basic.forever(function () {
    let p: number;
i = my_pins.length - 1
    while (i >= 0) {
        p = my_pins[i]
        pins.digitalWritePin(p, 1)
pause(100)
pins.digitalWritePin(p, 0)
i += 0 - 1
    }
})
