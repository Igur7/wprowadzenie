
from machine import Pin
from time import sleep_us

buzzer_a = Pin(10, Pin.OUT)
buzzer_b = Pin(11, Pin.OUT)

leds = [Pin(i, Pin.OUT) for i in (16, 17, 18, 19)]

song = [
    # Jeszcze Polska nie zginela
    (370, 210, 0),
    (415, 70, 0),
    (440, 280, 0),
    (440, 280, 0),

    # Kiedy my zyjemy
    (440, 210, 0),
    (440, 70, 0),
    (494, 140, 0),
    (440, 140, 0),
    (415, 140, 0),
    (370, 140, 0),

    (330, 210, 0),
    (330, 70, 0),
    (440, 420, 0),
    (415, 140, 0),
    (415, 280, 0),
    (370, 280, 280),

    # Co nam obca przemoc wziela
    (370, 210, 0),
    (415, 70, 0),
    (440, 280, 0),
    (440, 280, 0),

    (440, 210, 0),
    (440, 70, 0),
    (494, 140, 0),
    (440, 140, 0),
    (415, 140, 0),
    (370, 140, 0),

    # Szabla odbierzemy
    (330, 210, 0),
    (330, 70, 0),
    (440, 420, 0),
    (277, 140, 0),
    (330, 280, 0),
    (294, 280, 300),
]

# Refren - Marsz marsz Dabrowski
refren = [
    (330, 280, 0),
    (330, 420, 0),
    (415, 140, 0),
    (415, 280, 0),
    (370, 280, 280),

    # Z ziemi wloskiej do Polski
    (415, 210, 0),
    (415, 70, 0),
    (415, 280, 0),
    (415, 140, 0),
    (494, 140, 0),
    (494, 280, 0),
    (440, 280, 280),

    # Za twoim przewodem
    (370, 210, 0),
    (330, 70, 0),
    (587, 420, 0),
    (554, 140, 0),
    (554, 280, 0),
    (494, 280, 280),

    # Zlaczym sie z narodem
    (330, 210, 0),
    (330, 70, 0),
    (440, 420, 0),
    (277, 140, 0),
    (330, 280, 0),
    (294, 280, 350),
]

# Refren odtwarzany dwa razy
song = song + refren + refren



from machine import Pin
from time import sleep_us

buzzer_a = Pin(10, Pin.OUT)
buzzer_b = Pin(11, Pin.OUT)

leds = [Pin(i, Pin.OUT) for i in (16, 17, 18, 19)]

def beep(freq, duration):
    half_period = int(500000 / freq)
    cycles = round(freq * duration / 1000)

    buzzer_a.value(0)
    buzzer_b.value(1)

    for i in range(cycles * 2):
        buzzer_a.toggle()
        buzzer_b.toggle()
        sleep_us(half_period)

    buzzer_a.value(0)
    buzzer_b.value(0)

# Odtworz hymn jeden raz
for i, (freq, duration, pause) in enumerate(song):
    for j in range(4):
        leds[j].value(1 if j == i % 4 else 0)

    beep(freq, duration)

    for led in leds:
        led.value(0)

    sleep_us(pause * 1000)

print("Koniec hymnu")
