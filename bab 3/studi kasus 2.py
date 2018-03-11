'''import pprint
kata = raw_input('Masukkan kata : ')
count = {}
for huruf in kata:
    count.setdefault(huruf, 0)
    count[huruf] = count[huruf] + 1
pprint.pprint(count)'''

import pprint
s=str(raw_input('Masukkan kata : '))
pprint.pprint({x:list(s).count(x) for x in list(s)})
