import os
import logging
import time
import datetime

import _modem



def main():

    lastrun = None

    logging.basicConfig(format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        filename=os.path.expanduser('~/modemctrl.log'),
                        level=logging.INFO)

    while True:
        now = datetime.datetime.now()
        # run every hour if we have already run once
        if lastrun is not None and now.minute != 0:
            time.sleep(30)
            continue

        lastrun = time.time()

        # don't run more than once every 10 minutes
        if (time.time() - lastrun) < 600.0:
            continue

        # if 5am, force a modem reboot
        if now.hour == 5:
            logging.info('Rebooting modem (force=True) ...')
            _modem.reboot()
            continue

        try:
            downloadSpeed = _modem.getDownloadSpeed()
        except Exception:
            # speedtest.ConfigRetrievalError -- no network connection
            continue
        logging.info('Download speed is: {0:.2f} Mbit/s'.format(downloadSpeed / 1024.0 / 1024.0))
        if _modem.isConnectionSlow(downloadSpeed=downloadSpeed):
            logging.info('Rebooting modem...')
            _modem.reboot()
            continue


if __name__ == '__main__':
    main()