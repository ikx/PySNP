import pySNP

sig = "application/python_test"
title = "Python Test"
icon = "!system-info"
text = "Hello world"
timeout = "10"
uid = ""
password = ""

pySNP.snRegister(sig, title)
pySNP.snNotify(sig, title, text)
pySNP.snVersion()
pySNP.snUnregister(sig)
