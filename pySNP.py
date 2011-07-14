#!/usr/bin/env python

import socket

__author__ = 'Shawn McTear'
__version__ = '0.0.1'

ip = '127.0.0.1'
port = 9887

def request(snp):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip, port))
    sock.send(snp + '\r\n')
    response(sock, snp)
    sock.close()

def response(sock, snp):
    resp = sock.recv(1024).rstrip('\r\n')
    #TODO: check resp for snp error codes, then display error
    print resp
    print snp
    print ''

def process(action, data, req, value):
    err = error(False, '0', '')
    snp = 'snp://' + action
    param = ''

    # Checks if data is required and if values are empty
    for d, r, v in zip(data, req, value):
        if r is True and len(v) > 0:
            param = param + '&' + d + v
        elif r is True and len(v) <= 0:
            err = error(True, '109', d)
        elif r is False and len(v) > 0:
            param = param + '&' + d + v
        elif r is False and len(v) <= 0:
             param = param
        else:
            error(True, '', '')

    # Checks for errors before sending
    if err == False:
        param = param.replace('&', '?', 1)
        snp = snp + param
    request(snp)

def error(status, code, obj):
    if status is False and code is '0':
        return False
    elif status is True and code is '109':
        print 'Error: "%s" is missing.' % obj
        return True
    else:
        print 'Error: Unknown'
        return True

def snRegister(sig, password, title, icon):
    print 'Snarl: Register'
    action = 'register'
    data = ['app-sig=', 'password=', 'title=', 'icon=']
    req = [True, False, True, False]
    value = [sig, password, title, icon]
    process(action, data, req, value)

def snNotify(sig, uid, password, title, text, icon, cid, timeout, priority):
    print 'Snarl: Notify'
    action = 'notify'
    data = ['app-sig=', 'uid=', 'password=', 'title=', 'text=', 'icon=', 'id=', 'timeout=', 'priority=']
    req = [True, False, False, True, True, False, False, False, False]
    value = [sig, uid, password, title, text, icon, cid, timeout, priority]
    process(action, data, req, value)

def snAddClass(sig, password, title, text, icon, cid, name, enabled):
    print 'Snarl: AddClass'
    action = 'addclass'
    data = ['app-sig=', 'password=', 'title=', 'text=', 'icon=', 'id=', 'name=', 'enabled=']
    req = [True, False, False, False, False, True, True, False]
    value = [sig, password, title, text, icon, cid, name, enabled]
    process(action, data, req, value)

def snVersion():
    print 'Snarl: Version'
    action = 'version'
    data = []
    req = []
    value = []
    process(action, data, req, value)

def snUnregister(sig, password):
    print 'Snarl: Unregister'
    action = 'unregister'
    data = ['app-sig=', 'password=']
    req = [True, False]
    value = [sig, password]
    process(action, data, req, value)
