import sys
import socket

host = "127.0.0.1"
port = 9887

def request(action):
    action = action + "\r\n"
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.send(action)
    print sock.recv(1024), action
    sock.close()

def snRegister (sig, title, icon="", password=""):
    print "Snarl: Register"
    action = "snp://register?"
    if sig != "" :
        action = action + "app-sig=" + sig
    if title != "":
        action = action + "&title=" + title
    if icon != "":
        action = action + "&icon=" + icon
    if password != "":
        action = action + "&password=" + password
    request(action)

def snNotify (sig, title, text, icon="", timeout="10", uid="", password=""):
    print "Snarl: Notify"
    action = "snp://notify?"
    if sig != "" :
        action = action + "app-sig=" + sig
    if title != "":
        action = action + "&title=" + title
    if text != "":
        action = action + "&text=" + text
    if icon != "":
        action = action + "&icon=" + icon
    if timeout == "" or timeout != "":
        action = action + "&timeout=" + timeout
    if uid != "":
        action = action + "&uid=" + uid
    if password != "":
        action = action + "&password=" + password
    request(action)

def snVersion():
    print "Snarl: Version"
    action = "snp://version"
    request(action)

def snUnregister(sig, password=""):
    print "Snarl: Unregister"
    action = "snp://unregister?"
    if sig != "" :
        action = action + "app-sig=" + sig
    if password != "":
        action = action + "&password=" + password
    request(action)
