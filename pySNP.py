#!/usr/bin/env python

import socket

__author__ = 'Shawn McTear'
__version__ = '0.0.4'

class pySNP(object):
    ip = '127.0.0.1'
    port = 9887

    def __init__(self, **host):

        if 'ip' in host:
            self.ip = host['ip']
        if 'port' in host:
            self.ip = host['port']

    def _request(self, snp, errors):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            self.sock.connect((self.ip, self.port))
            self.sock.send(snp + '\r\n')
            recv = self.sock.recv(1024).rstrip('\r\n')
            self.sock.close()
            self._response(recv, errors, snp)
        except:
            errors = self._error(1, 'noserver', None, None)
            self._error(2, None, errors, None)
        print ''

    def _response(self, recv, errors, snp):
        print recv
        self._error(2, None, errors, None)
        print snp

    def _process(self, action, data, args):
        errors = self._error()
        snp = 'snp://' + action
        param = ''

        # Fills data with info from args if needed
        for d in data:
            if d in args:            
                x = data[d]
                x[2] = args[d]

        # Checks if data is required and if values are empty
        for key, value in sorted(data.items(), key=lambda x: x[1]):
            if value[1] is True and value[2]:
                param = param + '&' + key + '=' + value[2]
            elif value[1] is True and not value[2]:
                errors = _error(1, 'missing', errors, key)
            elif value[1] is False and value[2]:
                param = param + '&' + key + '=' + value[2]
            else:
                pass

        # Checks for errors before sending
        if not errors:
            param = param.replace('&', '?', 1)
            snp = snp + param
        self._request(snp, errors)

    def _error(self, mode=0, issue=None, errors=None, obj=None):
        pass
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

    def snRegister(self, appsig='', title='', **args):
        print 'Snarl: Register'
        action = 'register'
        data = {'app-sig': [1, True, appsig],
                'password': [2, False, ''],
                'title': [3, True, title],
                'icon': [4, False, '']}
        self._process(action, data, args)

    def snNotify(self, appsig='', title='', text='', **args):
        print 'Snarl: Register'
        action = 'notify'
        data = {'app-sig': [1, True, appsig],
                'password': [2, False, ''],
                'title': [3, True, title],
                'text': [4, True, text],
                'icon': [5, False, ''],
                'id': [6, False, ''],
                'uid': [7, False, ''],
                'timeout': [8, False, ''],
                'priority': [9, False, '']}
        self._process(action, data, args)

    def snAddClass(self, appsig='', cid='', cname='', **args):
        print 'Snarl: AddClass'
        action = 'addclass'
        data = {'app-sig': [1, True, appsig],
                'password': [2, False, ''],
                'title': [3, False, ''],
                'text': [4, False, ''],
                'icon': [5, False, ''],
                'id': [6, True, cid],
                'name': [7, True, cname],
                'enabled': [8, False, '']}
        self._process(action, data, args)

    def snVersion(self, **args):
        print 'Snarl: Version'
        action = 'version'
        data = {}
        self._process(action, data, args)

    def snUnregister(self, appsig='', **args):
        print 'Snarl: Unregister'
        action = 'unregister'
        data = {'app-sig': [1, True, appsig],
                'password': [2, False, '']}
        self._process(action, data, args)
