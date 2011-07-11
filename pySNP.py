import socket

host = "127.0.0.1"
port = 9887
print "Address:", host, ":", port

def request(action):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.send(action)
    print sock.recv(1024)
    sock.close()

def snRegister (sig, title, icon, password):
    print "Snarl: Register"
    action = ("snp://reg?app-sig=" + sig + "&title=" + title + "&icon=" +
              icon + "&password=" + password + "\r\n")
    request(action)
    
def snNotify (sig, title, text, icon, timeout, uid, password):
    print "Snarl: Notify"
    action = ("snp://notify?app-sig=" + sig + "&title=" + title + "&text=" +
              text + "&icon=" + icon + "&timeout=" + timeout + "&uid=" + uid +
              "&password=" + password + "\r\n")
    request(action)

def snVersion():
    print "Snarl: Version"
    action = "snp://version" + "\r\n"
    request(action)

def snUnregister(sig, password):
    print "Snarl: Unregister"           
    action = "snp://unreg?app-sig=" + sig + "&password=" + password + "\r\n"
    request(action)
