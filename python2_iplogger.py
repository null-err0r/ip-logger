#! /usr/bin/python2
# -*- coding: utf-8 -*-


import os ,time ,sys ,requests
import subprocess as sub

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=30, cols=60))

os.system('clear')

fn = "ip-log.txt"  
fp = os.path.join(os.path.dirname(__file__), fn)


r = os.system('ping -c 1 8.8.8.8 > /dev/null')
if (r == 0): 
    while True:
            ip1 = sub.Popen(["curl ident.me"],stdout=sub.PIPE,stderr=sub.PIPE, shell=True)
            output, errors = ip1.communicate(str.encode(" utf-8 "))
            file = open(fp, 'a')
            file.write(output + ' ' + time.strftime(" %H:%M:%S %Y-%m-%d ") + '\n')
            file.close
            print "\n Your IP: " + output + "   Time: " + time.strftime(" %H:%M:%S %Y-%m-%d ")

            time.sleep (30)
            ip2 = sub.Popen(["curl ident.me"],stdout=sub.PIPE,stderr=sub.PIPE, shell=True)
            output1, errors = ip2.communicate(str.encode(" utf-8 "))
            if output == output1:
                     print " "

            else :
		  ip3 = output1
		  data = ( "IP changed to: " + output1 + " -|-  time: " + time.strftime(" %H:%M:%S %Y-%m-%d ") + "\n" )
		  file = open(fp, 'a')
		  file.write(data)
		  file.close
		  print " IP Changed in: " + time.strftime(" %H:%M:%S %Y-%m-%d ") 
		  print " Previous IP \n " + output + " \n New IP \n " + ip3 


	
else :
      print "No internet connection"
      file = open(fp, 'a')
      file.write ( "No internet connection" + " - " + time.strftime(" %H:%M:%S %Y-%m-%d ") + "\n" )
      file.close		
	    

