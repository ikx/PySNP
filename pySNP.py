import socket

ip = '127.0.0.1'
port = 9887

def request(snp):
    snp = snp  + '\r\n'
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip, port))
    sock.send(snp)
    print sock.recv(1024), snp
    sock.close()

def action(snp, required, data, value):
    err = False
    q = ''
    for r, d, v in zip(required, data, value):
        if r != '' and v != '':
            q = q + d + v
        elif r != '' and v == '':
            print 'Error: "%s" is missing.' % d
            err = True
        elif v != '':
            q = q + d + v
    if err == False:
        snp = snp + q
    request(snp)

def snRegister(sig, token, title, icon, password):
    print 'Snarl: Register'
    snp = 'snp://register'
    required = ['?app-sig=', '',  '&title=', '', '']
    data = ['?app-sig=', '&token=', '&title=', '&icon=', '&password=']
    value = [sig, token, title, icon, password]
    action(snp, required, data, value)

def snNotify(sig, token, title, text, icon, timeout, priority, uid, password):
    print 'Snarl: Notify'
    snp = 'snp://notify'
    required = ['?app-sig=', '',  '&title=', '&text=', '', '', '', '', '']
    data = ['?app-sig=', '&token=','&title=', '&text=', '&icon=', '&timeout=',
            '&priority=', '&uid=', '&password=']
    value = [sig, token, title, text, icon, timeout, priority, uid, password]
    action(snp, required, data, value)

def snVersion():
    print 'Snarl: Version'
    snp = 'snp://version'
    request(snp)
 
def snUnregister(sig, token, password):
    print 'Snarl: Unregister'
    snp = 'snp://unregister'
    required = ['?app-sig=', '', '']
    data = ['?app-sig=', '&token=', '&password=']
    value = [sig, token, password]
    action(snp, required, data, value)
