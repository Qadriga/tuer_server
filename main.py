"""
main file of the RGH Door opening Project this implements the main loop
"""


#todo make wrapper class fot the rfid tags
import signal
import sys
import dbconnection
def Shutdown():
    """
    function to shutdown the application
    :return:
    """
    raise KeyboardInterrupt
signal.signal(signal.SIGINT,Shutdown()) # attach the signale hander for shutdown to CTRL+C



while True:
    try:
        dbconnection.check_user()
    except KeyboardInterrupt:
        sys.exit(0)