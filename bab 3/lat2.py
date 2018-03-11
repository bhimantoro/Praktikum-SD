Eng2Por = {'go':'ir', 'eat':'comer', 'store':'loja', \
             'thank you':'obrigado', 'university':'universidade', \
             'drink':'beber', 'shirt':'camisa', 'shoe':'sapato',\
             'home':'casa','mosque':'mesquita'}
Por2Eng = {'ir':'go','comer':'eat','loja':'store',\
             'obrigado':'thank you','universidade':'university',\
             'beber':'drink','camisa':'shirt','sapato':'shoe',\
             'casa':'home','mesquita':'mosque'}

def line_break():
    print '\n' * 5

def input():
    x=str(raw_input('Masukkan kata: '))

def English2Portugis():
    x=str(raw_input('Masukkan kata: '))
    x in Eng2Por
    print Eng2Por.get(x)

def Portugis2English():
    y=str(raw_input('Masukkan kata: '))
    y in Por2Eng
    print Por2Eng.get(y)

def menu():
    while True:
        line_break()
        print 'Kamus 2 Milyar : \n' \
          '1. Kamus Inggris ke Portugis\n' \
          '2. Kamus Portugis ke Inggris'
        pil = raw_input('Masukkan Menu Pilihan : ')
        if pil == '1':
            print 'Kamus Inggris ke Portugis'
            line_break()
            English2Portugis()
        elif pil == '2':
            print 'Kamus Portugis ke Inggris'
            line_break()
            Portugis2English()
        else:
            break

menu()
