"""
main file of the RGH Door opening Project this implements the main loop
"""


# todo make wrapper class fot the rfid tags
import signal
import sys
import dbconnection
import RPi.GPIO as GPIO
#import RPIO as GPIO
import time
import LCD_I2C.lcd as lcd
import RFID.MFRC522


interrupt = None
RFID_Reader = RFID.MFRC522.MFRC522()
lcd.initialize()
lcd.clear()


def shutdown(*args):
    """
    function to shutdown the application
    :return:
    """
    raise KeyboardInterrupt


def load_config():
    """
    function which load config parms into the program
    :return:
    """
    pass  # dummy


def chip_check_isr(GPIO_id, value):
    """
    Interrupt service Rutine for GPIO Interrupt
    :param GPIO_id: Number of the GPIO pin
    :param value: Value of the Singal on the Pin( 0 = Low, 1 = high)
    :return: no return value
    """
    pass  # Dummy


def poll_signal():
    """
    polling loop, this will check if
    :return:
    """
    lcd.backlight()
    lcd.printString("Ready for Duty", 0)
    time.sleep(2)
    lcd.clear()
    lcd.noBacklight()

    while True:
        time.sleep(0.1)
        (status, TagType) = RFID_Reader.MFRC522_Request(RFID.MFRC522.MFRC522.PICC_REQIDL)
        if status == RFID_Reader.MI_OK:
            lcd.backlight()
            lcd.clear()
            lcd.printString("Check RFID-Tag", 0)
            status, rfid = RFID_Reader.MFRC522_Anticoll()
            if status == RFID_Reader.MI_OK:
                if dbconnection.check_user(rfid):  # this will return true if id is valid
                    lcd.printString("Welcome :-)", lcd.LINE_1)
                    lcd.printString("Door will open", lcd.LINE_2)
                    for i in range(0, 5):
                        lcd.noBacklight()
                        time.sleep(0.5)
                        lcd.backlight()
                        time.sleep(0.5)
                else:
                    lcd.printString("Invalid Tag", lcd.LINE_1)
                    lcd.printString("Door will not open", lcd.LINE_2)
                    time.sleep(5)
            else:
                lcd.printString("Error while Reading", lcd.LINE_1)
                time.sleep(5)
            lcd.clear()
            lcd.noBacklight()






signal.signal(signal.SIGINT, shutdown)  # attach the signal handler for shutdown to CTRL+C

try:
    poll_signal()
except KeyboardInterrupt:
    sys.exit(0)

