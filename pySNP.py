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

def snRegister(sig, title, icon, password):
    print "Snarl: Register"
    snp = "snp://register?"
    data = ['app-sig=', '&title=', '&icon=', '&password=']
    value = [sig, title, icon, password]
    for v, d in zip(value, data):
        if v != "":
            r = d + v
            snp = snp + r
    request(snp)

def snNotify(sig, title, text, icon, timeout, priority, uid, password):
    print "Snarl: Notify"
    snp = "snp://notify?"
    data = ['app-sig=', '&title=', '&text=', '&icon=', '&timeout=', '&priority=', '&uid=', '&password=']
    value = [sig, title, text, icon, timeout, priority, uid,  password]
    for v, d in zip(value, data):
        if v != "":
            r = d + v
            snp = snp + r
    request(snp)

def snVersion():
    print "Snarl: Version"
    snp = "snp://version"
    request(snp)
 
def snUnregister(sig, password):
    print "Snarl: Unregister"
    snp = "snp://unregister?"
    data = ['app-sig=', '&password=']
    value = [sig, password]
    for v, d in zip(value, data):
        if v != "":
            r = d + v
            snp = snp + r
    request(snp)
