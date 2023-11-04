import machine
import utime

button_pins = [6, 7, 8, 9, 10, 11, 12]
buzzer_pin = 16

frequencies = {
    'DO': 261.63,
    'RE': 293.66,
    'MI': 329.63,
    'FA': 349.23,
    'SOL': 392.00,
    'LA': 440.00,
    'TI': 493.88,
}


buttons = [machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_UP) for pin in button_pins]

buzzer = machine.PWM(machine.Pin(buzzer_pin))

def play_tone(frequency, duration):
    buzzer.duty_u16(512)
    buzzer.freq(int(frequency))
    utime.sleep_ms(duration)
    buzzer.duty_u16(0)

while True:
    for i, button in enumerate(buttons):
        if button.value() == 0:
            note = list(frequencies.keys())[i]
            frequency = frequencies[note]
            print("Button {} ({}): Playing {}".format(i, note, note))
            play_tone(frequency, 200)
    utime.sleep(0.1)
