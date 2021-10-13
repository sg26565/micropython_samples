from machine import Pin, idle

class Button:
    """"A debouncing button."""    
    def __init__(self, pin: Pin, handler: function = None, bounce_delay: int = 3):
        self.pin = pin
        self.value = pin.value()
        self.debounce = 0
        self.handler = handler
        self.bounce_delay = bounce_delay

    def poll(self):
        """Poll current state of button and handle event after debounce delay."""
        actual = self.pin.value()

        if actual != self.value:
            self.debounce += 1

            if self.debounce > self.bounce_delay:
                self.debounce = 0
                self.value = actual
                if self.handler:
                    self.handler(self)


def sw_handler(button: Button):
    """Handle switch press/release."""
    global rotary_value

    if button.value == 0:
        print('Button pressed')
    else:
        print('Button released')
        rotary_value = 0
        print('Rotary value', rotary_value)


def rotary_handler(button: Button):
    """Handle rotary move."""
    global rotary_value

    if button.value == 0:
        if dt.value == 1:
            rotary_value += 1
        else:
            rotary_value -= 1

        print('Rotary value', rotary_value)

sw = Button(Pin(4, Pin.IN, Pin.PULL_UP), sw_handler)
dt = Button(Pin(23, Pin.IN, Pin.PULL_UP))
clk = Button(Pin(22, Pin.IN, Pin.PULL_UP), rotary_handler)
rotary_value = 0

print('Rotary value', rotary_value)
while True:
    sw.poll()
    clk.poll()
    dt.poll()
    idle()
