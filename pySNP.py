#!/usr/bin/env python

import socket

__author__ = 'Shawn McTear'
__version__ = '0.0.3'

ip = '127.0.0.1'
port = 9887

def _request(snp, errors):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        sock.connect((ip, port))
        sock.send(snp + '\r\n')
        _response(sock, snp, errors)
        sock.close()
    except:
        errors = _error(1, 'noserver', None, None)
        _error(2, None, errors, None)
    print ''

def _response(sock, snp, errors):
    resp = sock.recv(1024).rstrip('\r\n')
    print resp
    _error(2, None, errors, None)
    print snp

def _process(action, data, value, req):
    errors = _error()
    snp = 'snp://' + action
    param = ''

    #Checks if data is required and if values are empty
    for d, v, r in zip(data, value, req):
        if r is True and v:
            param = param + '&' + d + v
        elif r is True and not v:
            errors = _error(1, 'missing', errors, d)
        elif r is False and v:
            param = param + '&' + d + v
        else:
            pass

    #Checks for errors before sending
    if not errors:
        param = param.replace('&', '?', 1)
        snp = snp + param
    _request(snp, errors)

def _error(mode=0, issue=None, errors=None, obj=None):
    issue = issue or ''
    errors = errors or []
    obj = obj or ''

    if mode is 1 and issue is 'missing':
        error = "*Error: '%s' is missing.*" % obj
        errors.append(error)
    elif mode is 1 and issue is 'noserver':
        error = "*Error: Can't connect to Snarl.*"
        errors.append(error)
    elif mode is 2:
        for error in errors:
            print error
    else:
        pass
    return errors

def snRegister(sig, password, title, icon):
    print 'Snarl: Register'
    action = 'register'
    data = ['app-sig=', 'password=', 'title=', 'icon=']
    value = [sig, password, title, icon]
    req = [True, False, True, False]
    _process(action, data, value, req)

def snNotify(sig, password, title, text, icon, cid, uid, timeout, priority):
    print 'Snarl: Notify'
    action = 'notify'
    data = ['app-sig=', 'password=', 'title=', 'text=', 'icon=', 'id=',
            'uid=', 'timeout=', 'priority=']
    value = [sig, password, title, text, icon, cid, uid, timeout, priority]
    req = [True, False, True, True, False, False, False, False, False]
    _process(action, data, value, req)

def snAddClass(sig, password, title, text, icon, cid, name, enabled):
    print 'Snarl: AddClass'
    action = 'addclass'
    data = ['app-sig=', 'password=', 'title=', 'text=', 'icon=', 'id=',
            'name=', 'enabled=']
    value = [sig, password, title, text, icon, cid, name, enabled]
    req = [True, False, False, False, False, True, True, False]
    _process(action, data, value, req)

def snVersion():
    print 'Snarl: Version'
    action = 'version'
    data = []
    value = []
    req = []
    _process(action, data, value, req)

def snUnregister(sig, password):
    print 'Snarl: Unregister'
    action = 'unregister'
    data = ['app-sig=', 'password=']
    value = [sig, password]
    req = [True, False]
    _process(action, data, value, req)
