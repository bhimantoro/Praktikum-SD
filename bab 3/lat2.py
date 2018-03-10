x=str(raw_input('Masukkan kata: '))
Eng2Spain = {'go':'ir', 'eat':'comer', 'store':'loja', \
             'ty':'obrigado', 'university':'universidade', \
             'drink':'beber', 'shirt':'camisa', 'shoe':'sapato',\
             'home':'casa','mosque':'mesquita'}
x in Eng2Spain
print(Eng2Spain.get(x))

