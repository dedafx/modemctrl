__all__ = ['setSpeedTreshold', 'isConnectionSlow', 'getDownloadSpeed']

import speedtest


SPEED_THRESHOLD = 80.0 * 1024 * 1024 # 80 Mbps


def setSpeedTreshold(threshold):
    """
    Set the speed threshold to test connection speed against.
    """
    global SPEED_THRESHOLD
    SPEED_THRESHOLD = threshold


def isConnectionSlow(threshold=SPEED_THRESHOLD, downloadSpeed=None):
    """
    Return true|false if the connection is slower than the given threshold.
    """
    if downloadSpeed is None:
        downloadSpeed = getDownloadSpeed()
    return downloadSpeed < threshold


def getDownloadSpeed():
    """
    Check the download speed of the network connection. Return the value.
    """
    st = speedtest.Speedtest()
    return st.download()
