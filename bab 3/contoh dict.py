ba = {'andi': 'andi@python.org',\
    'bella': 'bella@rocket.org',\
    'doni': 'doni@domain.org',}
print 'alamat email andi:', ba['andi']
del ba['doni']
print 'ada %s kontak di buku alamat' %len(ba)
for nama, email in ba.items():
    print '%s, email: %s' % (nama, email)
ba['evan']='evan@evandian.org'
if 'evan' in ba:
    print 'Email evan di', ba['evan']
