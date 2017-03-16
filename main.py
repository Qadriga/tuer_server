"""
main file of the RGH Door opening Project this implements the main loop
"""



#todo make wrapper class fot the rfid tags
import signal
import sys
import dbconnection
#  import RPi.GPIO as GPIO
import RPIO as GPIO

def Shutdown():
    """
    function to shutdown the application
    :return:
    """
    raise KeyboardInterrupt
def chip_check_isr(GPIO_id, value):
    """
    Interrupt service Rutine for GPIO Interrupt
    :param GPIO_id: Number of the GPIO pin
    :param value: Value of the Singal on the Pin( 0 = Low, 1 = high)
    :return: no return value
    """
    pass  # Dummy

signal.signal(signal.SIGINT, Shutdown())  # attach the signale hander for shutdown to CTRL+C

# GPIO Pins
Interrupt_port = 0

# varibaels for Interrupting
Interrupt_edge = 'both'  # allowed values are 'both', 'rising', 'falling'

GPIO.setmode(GPIO.BCM)
GPIO.setup(Interrupt_port, GPIO.IN)
GPIO.add_interrupt_callback(Interrupt_port, chip_check_isr, Interrupt_edge, debounce_timeout_ms=3000)
# attach the Interrupt handler only one interrupt every 3 seconds

try:
    GPIO.wait_for_interrupts()  # Let the Script run into a endless main loop
except KeyboardInterrupt:
    GPIO.stop_waiting_for_interrupts()  # stop waiting for interrupts
    GPIO.cleanup()  # Clean up GPIO
    sys.exit(0)

