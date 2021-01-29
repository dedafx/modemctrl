# modemctrl
Use speedtest download speeds to control rebooting a cable modem via relay and raspberry pi.

Does your cable provider throttle your service periodically, forcing you to reboot the modem to get the internet speeds that you pay for? Well, so do I! I got so tierd of rebooting the modem, hoping to do it while the fam is out of WFH and remote school, that I made a device to reboot it for me. Using a Raspberry Pi 4 and a relay connected to the gpio pins, we can use a python script to query the internet speed and power cycle the cable modem to get our service back. I am paying for the service, and damn it, I'm going to get what I am paying for, cable provider!


# Hardware
Raspberry Pi 4 https://www.raspberrypi.org/products/raspberry-pi-4-model-b/
Relay Module   https://www.amazon.com/gp/product/B00LW15A4W
DC plug extension that fits your cable modem
Cable Modem

