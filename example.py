import pySNP

sig = "application/python_test"
print sig
title = "Python Test"
icon = "!system-info"
text = "Hello world"
timeout = "10"
uid = ""
password = ""

pySNP.snRegister(sig, title, icon, password)
pySNP.snNotify(sig, title, text, icon, timeout, uid, password)

pySNP.snVersion()
pySNP.snUnregister(sig, password)
