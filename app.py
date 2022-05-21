## importing socket module
import socket
import os
import subprocess

import flask

def wlan_ip():
    import subprocess
    result=subprocess.run('ipconfig',stdout=subprocess.PIPE,text=True).stdout.lower()
    scan=0
    for i in result.split('\n'):
        if 'wireless' in i: scan=1
        if scan:
            if 'ipv4' in i: return i.split(':')[1].strip()

ip = wlan_ip()
command = "artisan.bat %s" % (ip)
flaskCommand = "flask.bat %s" % (ip)
process = subprocess.Popen([r'nodemon.bat'],  creationflags=subprocess.CREATE_NEW_CONSOLE)
process2 = subprocess.Popen(command.split(),  creationflags=subprocess.CREATE_NEW_CONSOLE, stdout=subprocess.PIPE)
flaskProcess = subprocess.Popen(flaskCommand.split(),  creationflags=subprocess.CREATE_NEW_CONSOLE, stdout=subprocess.PIPE)
process.wait()
process2.wait()
flaskProcess.wait()