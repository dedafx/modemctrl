import os
import logging
import time
import datetime

from dedafx import modemctrl



def main():

    lastrun = None

    while True:
        now = datetime.datetime.now()
        if lastrun is not None and now.minute != 0:
            time.sleep(5)
            continue

        lastrun = time.time()
        logging.basicConfig(format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            filename=os.path.expanduser('~/modemctrl.log'),
                            level=logging.INFO)

        if now.hour == 5:
            logging.info('Rebooting modem (force=True) ...')
            modemctrl.reboot()
            continue

        downloadSpeed = modemctrl.getDownloadSpeed()
        logging.info('Download speed is: {0:.2f} Mbit/s'.format(downloadSpeed / 1024.0 / 1024.0))
        if modemctrl.isConnectionSlow(downloadSpeed=downloadSpeed):
            logging.info('Rebooting modem...')
            modemctrl.reboot()
            continue


if __name__ == '__main__':
    main()