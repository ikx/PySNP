import pysnp

sn = pysnp.PySNP()

sn.register('SIG', 'TITLE', password='testPASS', icon='testICON')
sn.notify('SIG', 'TITLE', 'TEXT', password='testPASS', icon='testICON')
sn.addclass('SIG', 'CID', 'CNAME', password='testPASS')
sn.version()
sn.unregister('SIG', password='testPASS')

#x = raw_input('Hit ANY key to exit')
