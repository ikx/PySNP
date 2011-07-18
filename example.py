import pySNP    

snarl = pySNP.pySNP()

snarl.snRegister('SIG', 'TITLE', password='testPASS', icon='testICON')
snarl.snNotify('SIG', 'TITLE', 'TEXT', password='testPASS', icon='testICON')
snarl.snAddClass('SIG', 'CID', 'CNAME', password='testPASS')
snarl.snVersion()
snarl.snUnregister('SIG', password='testPASS')


#x = raw_input('Hit ANY key to exit')
