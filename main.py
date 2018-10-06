"""
main file of the RGH Door opening Project this implements the main loop
"""


# todo make wrapper class fot the rfid tags
import signal # singal handelers
import sys # system functions
import dbconnection # database module
import ssh_tunnel # ssh tunnel module
import RPi.GPIO as GPIO #gpio module
#import RPIO as GPIO
import time
import LCD_I2C.lcd as lcd
import RFID.MFRC522


interrupt = None
DOORPIN = 9
RFID_Reader = RFID.MFRC522.MFRC522()

lcd.initialize()  # start the lcd display
lcd.clear()
#setup the gpio pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(DOORPIN, GPIO.OUT)
if ssh_tunnel.TUNNEL is None:
    ssh_tunnel.SSHTunnelWrapper()  # start the ssh tunnel wrapper for the conection

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

def open_door():
    """
    function witch is called to open the door by set one pin to 1 for a specific time
    :return:
    """
    GPIO.output(DOORPIN,GPIO.UP)


def lock_door():
    """
    locks the door by setting a pin to 0
    :return:
    """
    GPIO.output(DOORPIN, GPIO.DOWN)

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
        time.sleep(0.2)
        (status, TagType) = RFID_Reader.MFRC522_Request(RFID.MFRC522.MFRC522.PICC_REQIDL)
        if status == RFID_Reader.MI_OK:
            lcd.backlight()
            lcd.clear()
            lcd.printString("Check RFID-Tag", 0)
            status, rfid = RFID_Reader.MFRC522_Anticoll()
            if status == RFID_Reader.MI_OK:
                if dbconnection.check_user(rfid):  # rfid should be an array of substrings or this functuon will fail
                    #  this will return true if id is valid
                    lcd.printString("Welcome :-)", lcd.LINE_1)
                    lcd.printString("Door will open", lcd.LINE_2)
                    open_door()
                    for i in range(0, 5):
                        lcd.noBacklight()
                        time.sleep(0.5)
                        lcd.backlight()
                        time.sleep(0.5)
                    lock_door()
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
    dbconnection.validate_schema()  # check database
    poll_signal()
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit(0)

