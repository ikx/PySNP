import pySNP    

pySNP.snRegister('SIG', 'TITLE', password='testPASS', icon='testICON')
pySNP.snNotify('SIG', 'TITLE', 'TEXT', password='testPASS', icon='testICON')
pySNP.snAddClass('SIG', 'CID', 'CNAME', password='testPASS')
pySNP.snVersion()
pySNP.snUnregister('SIG', password='testPASS')


#x = raw_input('Hit ANY key to exit')
