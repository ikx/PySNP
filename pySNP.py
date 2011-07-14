#!/usr/bin/env python

import socket

__author__ = 'Shawn McTear'
__version__ = '0.0.2'

ip = '127.0.0.1'
port = 9887

def request(snp, err_msgs):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip, port))
    sock.send(snp + '\r\n')
    response(sock, snp, err_msgs)
    sock.close()

def response(sock, snp, err_msgs):
    resp = sock.recv(1024).rstrip('\r\n')
    print resp
    #TODO: check resp for snp error codes, then display error
    for err_msg in err_msgs:
        print err_msg
    print snp + '\n'

def process(action, data, req, value):
    err_msgs = error()
    snp = 'snp://' + action
    param = ''

    #Checks if data is required and if values are empty
    for d, r, v in zip(data, req, value):
        if r is True and len(v) > 0:
            param = param + '&' + d + v
        elif r is True and len(v) <= 0:
            err_msgs = error(True, err_msgs, d)
        elif r is False and len(v) > 0:
            param = param + '&' + d + v
        elif r is False and len(v) <= 0:
            pass

    #Checks for errors before sending
    if not err_msgs:
        param = param.replace('&', '?', 1)
        snp = snp + param
    request(snp, err_msgs)

def error(status=False, err_msgs=[], obj=''):
    if status is False:
        err_msgs = []
        return err_msgs
    elif status is True:
        err_msg = '*Error: "%s" is missing.*' % obj
        err_msgs.append(err_msg)
        return err_msgs

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
    data = ['app-sig=', 'uid=', 'password=', 'title=', 'text=', 'icon=',
            'id=', 'timeout=', 'priority=']
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
