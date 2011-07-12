import pySNP    

sig = "sig"
title = "title"
text = "text"
icon = ""
timeout = ""
priority = ""
uid = ""
password = ""

pySNP.snRegister(sig, title, icon, password)
pySNP.snNotify(sig, title, text, icon, timeout, priority, uid, password)
pySNP.snVersion()
pySNP.snUnregister(sig, password)
