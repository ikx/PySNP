import pySNP    

sig = "sig"
token = ""
title = "title"
text = "text"
icon = ""
timeout = ""
priority = ""
uid = ""
password = ""

pySNP.snRegister(sig, token, title, icon, password)
pySNP.snNotify(sig, token, title, text, icon, timeout, priority, uid, password)
pySNP.snVersion()
pySNP.snUnregister(sig, token, password)
