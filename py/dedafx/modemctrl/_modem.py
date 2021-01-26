import time
import gpiozero


RELAY_PIN = 23
INVERT_PIN = True
TIME_OFF = 30.0
pin = gpiozero.LED(pin)


def turnModemOn(invertPin=INVERT_PIN):
    """Turn the modem on."""
    if not invertPin:
        pin.on()
    else:
        pin.off()


def turnModemOff(invertPin=INVERT_PIN):
    """Turn the modem off."""
    if not invertPin:
        pin.off()
    else:
        pin.on()


def reboot(timeOff=TIME_OFF, invertPin=INVERT_PIN):
    """
    Reboot the modem using the given pin.
    Leave the modem off for the given ammount of time.
    invertPin is the off value is high, vs off is low (default).
    """
    turnModemOff(invertPin=invertPin)
    time.sleep(timeOff)
    turnModemOn(invertPin=invertPin)