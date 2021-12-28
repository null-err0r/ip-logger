#! /usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
import time , os ,requests , subprocess ,sys
import colorama
from colorama import Fore, Back, Style


colorama.init()
while True:
      try:
         if requests.get('https://google.com').ok:
                ip1 = urllib.request.urlopen('https://api.ipify.org').read()
                ip2 = urllib.request.urlopen('https://api.ipify.org').read()
                print (Fore.GREEN + "\nProgram is Running!\n Your IP adress: " + str(ip1.decode("utf-8")) + "   Time: " + time.strftime("%Y-%m-%d %H:%M") + Style.RESET_ALL)

                print ("\nList IP Connected\n")
                print(str(os.system("netstat -tn 2>/dev/null | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -nr | head").decode("utf-8")))
                time.sleep (30)
                if ip1 != ip2:
	                 ip3 = ip1
	                 ip1 = ip2
	                 data = (Fore.RED + 'Ip has changed while script is running, ip changed to ' + str(ip1.decode("utf-8")) + '     Detected when: ' + time.strftime("%Y-%m-%d %H:%M") + '\n' + Style.RESET_ALL)
	                 print (Fore.RED + time.strftime("%Y-%m-%d %H:%M") + ' IP CHANGED!\a' + Style.RESET_ALL)
	                 print (Fore.RED + str(ip3.decode("utf-8")) + ' WAS THE PREVIOUS IP! \n' + str(ip2.decode("utf-8")) + ' IS THE NEW IP\n\n' + Style.RESET_ALL)
	

      except:
            print("No internet connection")
            
