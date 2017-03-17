"""
main file of the RGH Door opening Project this implements the main loop
"""


# todo make wrapper class fot the rfid tags
import signal
import sys
import dbconnection
#  import RPi.GPIO as GPIO
import RPIO as GPIO
import time
import LCD_I2C.lcd as lcd
import RFID.MFRC522


interrupt = None
RFID_Reader = RFID.MFRC522.MFRC522()
lcd.initialize()
lcd.clear()


def shutdown():
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
            status, ID = RFID_Reader.MFRC522_Anticoll()
            if status == RFID_Reader.MI_OK:
                pass




signal.signal(signal.SIGINT, shutdown())  # attach the signal handler for shutdown to CTRL+C

# GPIO Pins
Interrupt_port = 0

# varibaels for Interrupting
Interrupt_edge = 'both'  # allowed values are 'both', 'rising', 'falling'

GPIO.setmode(GPIO.BCM)
if interrupt is True:
    GPIO.setup(Interrupt_port, GPIO.IN)
    GPIO.add_interrupt_callback(Interrupt_port, chip_check_isr, Interrupt_edge, debounce_timeout_ms=3000)
    # attach the Interrupt handler only one interrupt every 3 seconds

try:
    if interrupt is True:
        GPIO.wait_for_interrupts()  # Let the Script run into a endless main loop
    else:
        poll_signal()
except KeyboardInterrupt:
    if interrupt is True:
        GPIO.stop_waiting_for_interrupts()  # stop waiting for interrupts
    GPIO.cleanup()  # Clean up GPIO
    sys.exit(0)

