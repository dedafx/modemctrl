__all__ = ['setSpeedTreshold', 'isConnectionSlow']

import speedtest


SPEED_THRESHOLD = 80.0 * 1024 * 1024 # 80 Mbps


def setSpeedTreshold(threshold):
    """
    Set the speed threshold to test connection speed against.
    """
    global SPEED_THRESHOLD
    SPEED_THRESHOLD = threshold


def isConnectionSlow(threshold=SPEED_THRESHOLD):
    """
    Return true|false if the connection is slower than the given threshold.
    """
    return getDownloadSpeed() < threshold


def getDownloadSpeed():
    """
    Check the download speed of the network connection. Return the value.
    """
    st = speedtest.Speedtest()
    return st.download()
    