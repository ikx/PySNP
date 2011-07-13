#!/usr/bin/env python

__author__ = "Shawn McTear"

import socket

ip = '127.0.0.1'
port = 9887

def request(snp):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip, port))
    sock.send(snp + '\r')
    print sock.recv(1024) + snp + '\n'
    sock.close()

def process(snp, req, data, value):
    error = False
    param = ''

    # Checks if data is required and if values are empty
    for r, d, v in zip(req, data, value):
        if r is True and len(v) > 0:
            param = param + d + v
        elif r is True and len(v) <= 0:
            param = param + ''
            error = True
            print 'Error: "%s" is missing.' % d
        elif r is False and len(v) > 0:
            param = param + d + v
        elif r is False and len(v) <= 0:
            param = param + ''
        else:
            print 'Error: Unknown'

    # Checks if there where any errors before sending
    if error is False:
        snp = snp + param
    request(snp)

def snRegister(sig, token, title, icon, password):
    print 'Snarl: Register'
    snp = 'snp://register'
    req = [True, False, True, False, False]
    data = ['?app-sig=', '&token=', '&title=', '&icon=', '&password=']
    value = [sig, token, title, icon, password]
    process(snp, req, data, value)

def snNotify(sig, token, title, text, icon, timeout, priority, uid, password):
    print 'Snarl: Notify'
    snp = 'snp://notify'
    req = [True, False, True, True, False, False, False, False, False]
    data = ['?app-sig=', '&token=','&title=', '&text=', '&icon=', '&timeout=',
            '&priority=', '&uid=', '&password=']
    value = [sig, token, title, text, icon, timeout, priority, uid, password]
    process(snp, req, data, value)

def snVersion():
    print 'Snarl: Version'
    snp = 'snp://version'
    req = []
    data = []
    value = []
    process(snp, req, data, value)

def snUnregister(sig, token, password):
    print 'Snarl: Unregister'
    snp = 'snp://unregister'
    req = [True, False, False]
    data = ['?app-sig=', '&token=', '&password=']
    value = [sig, token, password]
    process(snp, req, data, value)
