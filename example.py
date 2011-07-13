import pySNP    

sig = 'SIG'
token = ''
title = 'TITLE'
text = 'TEXT'
icon = ''
timeout = ''
priority = ''
uid = ''
password = ''

pySNP.snRegister(sig, token, title, icon, password)
pySNP.snNotify(sig, token, title, text, icon, timeout, priority, uid, password)
pySNP.snVersion()
pySNP.snUnregister(sig, token, password)

x = raw_input('Hit ANY key to exit')
