#!/usr/local/bin/python
#coding=utf-8
import telnetlib
def mikroticconnect(num,mes):
    #import pdb; pdb.set_trace()
    host = '172.16.0.253'
    tn = telnetlib.Telnet(host)
    out = tn.read_until('Login: ',5)
    tn.write("admin\r\n")# Edit "admin" on your login
    out = tn.read_until('Password: ',5)
    tn.write("password1\r\n")# Edit "password1" on your password
    out = tn.read_until('[admin@LabZV] > ',10)
    from os import system
    from sys import platform
    if platform == 'win32':
        sleep = 'timeout /T 5 > NUL'
    else:
        sleep = 'sleep 5'
    system(sleep)
    gatemess = '/tool sms send port=usb1 channel=0 phone-number=' + num + ' message="' + mes + '" type=class-0\r\n'
    tn.write(gatemess)
    system(sleep)
    out = tn.read_until('[admin@LabZV] >',20)
    tn.close()
    return ''


if __name__ == '__main__':
    import sys
    num = str(sys.argv[1])
    mes = str(sys.argv[2])
    mikroticconnect(num,mes)
