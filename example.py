import pySNP    

sig = 'SIG'
uid = 'UID'
password = ''
title = 'TITLE'
text = 'TEXT'
icon = 'ICON'
cid = 'CID'
timeout = '10'
priority = 'PRIORITY'
name = 'NAME'
enabled = 'ENABLED'

pySNP.snRegister(sig, password, title, icon)
pySNP.snNotify(sig, uid, password, title, text, icon, cid, timeout, priority)
pySNP.snAddClass(sig, password, title, text, icon, cid, name, enabled)
pySNP.snVersion()
pySNP.snUnregister(sig, password)

x = raw_input('Hit ANY key to exit')
