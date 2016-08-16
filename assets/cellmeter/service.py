#License
#-------
#This code is published and shared by Numato Systems Pvt Ltd under GNU LGPL 
#license with the hope that it may be useful. Read complete license at 
#http://www.gnu.org/licenses/lgpl.html or write to Free Software Foundation,
#51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA

#Simplicity and understandability is the primary philosophy followed while
#writing this code. Sometimes at the expence of standard coding practices and
#best practices. It is your responsibility to independantly assess and implement
#coding practices that will satisfy safety and security necessary for your final
#application.

#This demo code demonstrates how to read the status of a GPIO


import sys
import serial  
import time
import util
import bluetooth
import subprocess
#import os


#portName = 'COM6'
portName = '/dev/rfcomm0'
gpioNum = '0'
feedback = ''
#username = os.getenv('username', 'lavashonline@gmail.com')
#password = os.getenv('password', 'sweety')

def bind_host(self):
        nearby_devices = bluetooth.discover_devices(lookup_names=True)
        for addr, name in nearby_devices:
                if name == "RNBT-B556":
                        host = addr
        cmd = 'echo osmc | sudo -S rfcomm bind 0'+ host
        output = subprocess.check_output(cmd,shell=True)
        return output


try:
        #util.hookcell().login(username,password)
        bind_host()
    
        serPort = serial.Serial(portName, 9600, timeout=30)
except:
        sys.exit(0)


serPort.write("gpio read "+ str(gpioNum) + "\r")
time.sleep(0.2)

while True:
                
        response = serPort.read(25)
        if(response.find("r1") > 0):
                feedback =  util.hookcell().receivevalue()
                
                if(feedback.find("off0") > 0):
                        serPort.write("relay write 0" + "\n\r")
                
                if(feedback.find("off1") > 0):
                        serPort.write("relay write 1" + "\n\r")
                
                        

              
serPort.close()
