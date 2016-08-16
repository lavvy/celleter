import urllib,urllib2,sys,re,json,os,cookielib,platform
import resources.lib.requests as requests
from xml.dom import minidom
import time

#import RPi.GPIO as GPIO



import httplib, datetime # added this for the emoncms update

scriptpath = sys.path[0]
meterpath = ''
if platform.system() =='Windows':
    meterpath = 'C:\\Users\\uche\\AppData\\Roaming\\Kodi\\addons\\'
    scriptpath = scriptpath + '\\'

else:
    meterpath = '/home/osmc/.kodi/addons/'
    scriptpath = scriptpath +'/'

logpath = meterpath +'hktok.tok'
email = "lavashonline@gmail.com"
password = "sweety"
token =      '0c1edce677cfb896c8263beb1a518d62'
site = 'http://hookcell.com'

u = os.getenv('username', 'la.com')
p = os.getenv('password', 'ety')

import os as os
import shutil as shutil
if os.path.isfile(meterpath +'current.txt'):
    pass
else:
    shutil.copy(scriptpath +'config.xml',meterpath +'config.xml')
    shutil.copy(scriptpath +'current.txt',meterpath +'current.txt')
    shutil.copy(scriptpath +'hour.txt',meterpath +'hour.txt')
    shutil.copy(scriptpath +'value.txt',meterpath +'value.txt')
    hookcell.login(u,p)
    
class hookcell():
    
##################### emoncms update hack
    pulsecount=0  
    power=0
#######################

    
    email = "lhonline@gmail.com"
    password = "sty"
    token =      '0c1edce677cfb896c8263beb1a518d62'
    site = 'http://hookcell.com'
    logpath = meterpath +'hktok.tok'





    
######### UPDATING TO EMONCMS SERVER ###########################
# Every minute this function converts the number of pulses over the last minute into a power value and sends it to EmonCMS
    #@sched.interval_schedule(minutes=1)
    def SendPulses():
	global pulsecount
	global power
#	print ("Pulses: %i") % pulsecount # Uncomment for debugging.
	# The next line calculates a power value in watts from the number of pulses, my meter is 1000 pulses per kWh, you'll need to modify this if yours is different.
	power = pulsecount * 60
#	print ("Power: %iW") % power # Uncomment for debugging.
	pulsecount = 0;
	timenow = time.strftime('%s')
        url = ("/emoncms/input/post?time=%s&node=1&json={power:%i}&apikey=<insert API key here>") % (timenow, power) # You'll need to put in your API key here from EmonCMS
        connection = httplib.HTTPConnection("localhost")
        connection.request("GET", url)

#####################################################################




 
 
    
    def login(self,u,p):
        payload = {
    'core[security_token]': self.token,
    'val[login]': u,
    'val[remember_me]': '',
    'password-clear': 'Combination',
    'val[password]': p
          }

        apikey = urllib.urlopen('http://hookcell.com/cellwalletapikey.txt').read()
        #import resources.lib.requests as requests
        with requests.Session() as s:
             f = 5
             s.post( self.site + '/index.php?do=/user/login/', data = payload)
             r = s.get( self.site + '/auth.php?key=' + apikey )
             asa = r.url
             token =  self.site + '/token.php?'+   asa[asa.find('key'):]
             result = s.get(token).text
             usertoken = result.partition('{"token":"')[2].partition('"}')[0]
             f = open(self.logpath,'w')
             f.write(usertoken)
             f.close()
        return usertoken
    
    def logout(self):
        with requests.Session() as s:
             usertoken = ""
             f = open(self.logpath,'w')
             f.write(usertoken)
             f.close()
        return usertoken 


    
    def gettoken(self):
        with requests.Session() as s:
             usertoken =""
             f = open(self.logpath,'r')
             usertoken = f.read()
             f.close()
        return usertoken 



    def loadcard(self,t):
        text = t
        parameters = urllib.urlencode({'token': self.gettoken() , 'method': 'videoplus.process', 'do': 'loadcredit', 'pin': text})
        result = urllib.urlopen(self.site +"/api.php?%s" % parameters)
        result = result.read()
        #result = json.loads(result)
        result = result.partition('"output":')[2].partition('}')[0]
        return 'You just funded your account and your total balance is '+ result 
        


    def buyitem(self,t):
        text = t
        parameters = urllib.urlencode({'token': self.gettoken() , 'method': 'videoplus.process', 'do': 'buyitem', 'itemid': text})
        result = urllib.urlopen(self.site +"/api.php?%s" % parameters)
        result = result.read()
        #result = json.loads(result)
        result = result.partition('"output":')[2].partition('}')[0]
        return 'You just paid for this item : '+ result 
        


    def cashback(self,a,f,t):
        parameters = urllib.urlencode({'token': self.gettoken() , 'method': 'videoplus.process', 'do': 'transfer', 'amount': a , 'from': f , 'to': t })
        result = urllib.urlopen(self.site +"/api.php?%s" % parameters)
        result = result.read()
        #result = json.loads(result)
        result = result.partition('"output":')[2].partition('}')[0]
        return  result 
        



    def receive(self,a,f,t):
        parameters = urllib.urlencode({'token': self.gettoken() , 'method': 'videoplus.process', 'do': 'transfer1', 'amount': a , 'from': f , 'to': t })
        result = urllib.urlopen(self.site +"/api.php?%s" % parameters)
        result = result.read()
        #result = json.loads(result)
        result = result.partition('"output":')[2].partition('}')[0]
        return result 
        




    def payperson(self,a,f,t):
        parameters = urllib.urlencode({'token': self.gettoken() , 'method': 'videoplus.process', 'do': 'transfer1', 'amount': a , 'from': f , 'to': t })
        result = urllib.urlopen(self.site +"/api.php?%s" % parameters)
        result = result.read()
        #result = json.loads(result)
        result = result.partition('"output":')[2].partition('}')[0]#.replace('\/', '/')
        return result 
        

    def verify(self,t):
        text = t
        parameters = urllib.urlencode({'token': self.gettoken() , 'method': 'videoplus.process', 'do': 'find', 'data': text})
        result = urllib.urlopen(self.site +"/api.php?%s" % parameters)
        result = result.read()
        #result = json.loads(result)
        result =  result.partition('"output":')[2].partition('}')[0]
        return  result 
        


    def balance(self):
        text = ""
        parameters = urllib.urlencode({'token': self.gettoken() , 'method': 'videoplus.process', 'do': 'loadcredit', 'pin': text})
        result = urllib.urlopen(self.site +"/api.php?%s" % parameters)
        result = result.read()
        #result = json.loads(result)
        result = result.partition('"output":')[2].partition('}')[0]
        return 'Your balance is '+ result 



    def receivevalue(self):
        d = 1
        v = 2
        m = 3
        feedback =  'ON=2'
        ########### error checker
        e = 4
        a = 1 # 1 UNIT CUURENT READING
        
        f = open(meterpath+'current.txt','r')
        c = f.read()
        g = int(c) + int(a)
        f = open(meterpath+'current.txt','w')
        f.write(str(g))

        f = open(meterpath+'hour.txt','r')
        c = f.read()
        c = int(c) 

        h= time.strftime("%H")
        h = int(h)
      
# calculating kilowatt hour
        if h<>c: 
         f = open(meterpath+'hour.txt','w')
         f.write(str(h)) 


         f = open(meterpath+'current.txt','r')
         e = f.read()
         f = open(meterpath+'current.txt','w')
         f.write('0') 


         xmldoc = minidom.parse(meterpath+'config.xml')
         itemlist = xmldoc.getElementsByTagName('item')
         s= itemlist[h].attributes['hour'].value

         if s == 'x':
          feedback = 'OFF=9' # switch off supply in pin 4
          #self.turn_off_supply()
         elif s <> 'x':
          k = int(e) * int(s)
          f = open(meterpath+'value.txt','r')
          v = f.read()
          n = int(v) + int(k)
          f = open(meterpath+'value.txt','w')
          f.write(str(n)) 


# checking for 24 hours
         if h==14: 
          j= "me"
          t= "me"
          f = open(meterpath+'value.txt','r')
          e = f.read()
          c = self.payperson(e,j,t) 
          d = c.partition('"day":')[2].partition(',')[0]
          v = c.partition('"value":')[2].partition(',')[0]
          m = c.partition('"config":"')[2].partition('"')[0]
          f = open(meterpath+'value.txt','w')
          f.write('0') 
          f = open(meterpath+'config.xml','r')#from source prod
          config = f.read()
          f = open(meterpath+'config.xml','w')
          f.write(config) 

        f.close()
        return feedback +"On day "+str(d)+" you used "+str(v)+" of electricity with "+ str(m)
    



    def loadcardc(self):
        self.cad= "Your account funding was successful and your balance is #5000"
        return self.cad
    

    def balancec(self):
        self.bal= "Your account balance is #5000"
        return self.bal
    

    def activate(self):
        self.act= "                  Active"
        return self.act
    

    def search(self):
        self.se= "Your search result : John Doe"
        return self.se
    
