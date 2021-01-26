import time
import gpiozero


RELAY_PIN = 23
INVERT_PIN = True
TIME_OFF = 30.0


def turnModemOn(pin=RELAY_PIN, invertPin=INVERT_PIN):
    """Turn the modem on."""
    pin = gpiozero.LED(pin)
    if not invertPin:
        pin.on()
    else:
        pin.off()


def turnModemOff(pin=RELAY_PIN, invertPin=INVERT_PIN):
    """Turn the modem off."""
    pin = gpiozero.LED(pin)
    if not invertPin:
        pin.off()
    else:
        pin.on()


def reboot(relayPin=RELAY_PIN, timeOff=TIME_OFF, invertPin=INVERT_PIN):
    """
    Reboot the modem using the given pin.
    Leave the modem off for the given ammount of time.
    invertPin is the off value is high, vs off is low (default).
    """
    turnModemOff(pin=relayPin, invertPin=invertPin)
    time.sleep(timeOff)
    turnModemOn(pin=relayPin, invertPin=invertPin)