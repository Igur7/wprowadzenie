import machine

# leds

def LedsInit():   
    leds=[machine.Pin(gpio,machine.Pin.OUT) for gpio in (16,17,18,19)]
    [led.value(0) for led in leds]
    return leds
    
def LedSet(pos):
    global leds
    leds[pos].value(1);
    
def LedClr(pos):
    global leds
    leds[pos].value(0);

# buttons
    

def KeysInit():
    return [
        machine.Pin(gpio, machine.Pin.IN, machine.Pin.PULL_UP)
        for gpio in (9,8,7,6)
    ]
    
def KeyRead(pos):
    global buttons    
    return not buttons[pos].value()

def ButRead(pos):
    return KeyRead(pos)

# potentiometr

def PotInit():   
    return machine.ADC(26)
    
def PotRead():
    global potentiometer    
    return potentiometer.read_u16()

# init

leds = LedsInit()
buttons = KeysInit()
potentiometer = PotInit()
