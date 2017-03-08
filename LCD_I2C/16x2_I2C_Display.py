
# -*- coding: utf-8 -*-
"""
16x2 I2C Display
Version 1.0.0
DELOARTS Research Inc.
Philip Delorenzo
02.05.2016

This script interacts with an 16x2 display wired on the I2C bus on the Raspberry Pi.
It prints the IP address of the Raspberry.
"""

import lcd
from time import sleep
from subprocess import *

def runCMD(cmd):
  com = Popen(cmd, shell=True, stdout=PIPE)
  shellOutput = com.communicate()
  return shellOutput[0]


##### MAIN ######################################################################################

if __name__ == "__main__":

  lcd.initialize()

  cmdIPwlan0 = "ip addr show wlan0 | grep inet |awk '{print $2}' | cut -d/ -f1"
  strIPwlan0 = runCMD(cmdIPwlan0)

  cmdIPeth0 = "ip addr show eth0 | grep inet |awk '{print $2}' | cut -d/ -f1"
  strIPeth0 = runCMD(cmdIPeth0)

  i = 0
  while i < 1:
  
    ### Zeige IP-Adresse von wlan0:
    lcd.printString("IP Address wlan0:", lcd.LINE_1)
    lcd.printString(strIPwlan0.split('\n')[0], lcd.LINE_2)
    sleep(3)
  
    ### Zeige IP-Adresse von eth0
    lcd.printString("IP Address eth0:", lcd.LINE_1)
    lcd.printString(strIPeth0.split('\n')[0], lcd.LINE_2)
    sleep(3)

    i = i+1
 
  lcd.clear()
  lcd.noBacklight()
