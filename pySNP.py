import socket

ip = "127.0.0.1"
port = 9887

def request(snp):
    snp = snp + "\r\n"
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip, port))
    sock.send(snp)
    print sock.recv(1024), snp
    sock.close()

def action(snp, data, value):
    for v, d in zip(value, data):
        if v != "":
            r = d + v
            snp = snp + r
    request(snp)

def snRegister(sig, token, title, icon, password):
    print "Snarl: Register"
    snp = "snp://register?"
    data = ['app-sig=', '&token=', '&title=', '&icon=', '&password=']
    value = [sig, token, title, icon, password]
    action(snp, data, value)

def snNotify(sig, token, title, text, icon, timeout, priority, uid, password):
    print "Snarl: Notify"
    snp = "snp://notify?"
    data = ['app-sig=', '&token=','&title=', '&text=', '&icon=', '&timeout=',
            '&priority=', '&uid=', '&password=']
    value = [sig, token, title, text, icon, timeout, priority, uid, password]
    action(snp, data, value)

def snVersion():
    print "Snarl: Version"
    snp = "snp://version"
    request(snp)
 
def snUnregister(sig, token, password):
    print "Snarl: Unregister"
    snp = "snp://unregister?"
    data = ['app-sig=', '&token=', '&password=']
    value = [sig, token, password]
    action(snp, data, value)
