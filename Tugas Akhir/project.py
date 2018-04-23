import string
alfabet = string.ascii_letters

def enkrip(pesan):
    global alfabet

    cipher = ''
    for i in pesan:
        if i in alfabet:
            k = alfabet.find(i)
            k = (k + 3)%100
            cipher = cipher+alfabet[k]
        else:
            cipher = cipher + i

    return cipher

def dekrip(cipher):
    global alfabet
    pesan = ''
    for i in cipher:
        if i in alfabet:
            k = alfabet.find(i)
            k = (k - 3)%26
            pesan = pesan+alfabet[k]
        else:
            pesan = pesan + i

    return pesan

encrypt = {}
decrypt = {}

while True:
    print('----------------------------\n'
          'Kamus Caesar Cipher\n'
          '----------------------------')
    pilihan = int(raw_input('1. Enkripsi\n'
                            '2. Dekripsi\n'
                            '3. Kamus Enkripsi\n'
                            '4. Kamus Dekripsi\n'
                            '----------------------------\n'
                            'Pilih mode\t: '))
    if pilihan == 1:
        pesan = raw_input('Masukkan pesan\t: ')
        print(enkrip(pesan))
        encrypt[enkrip(pesan)]=pesan
    elif pilihan == 2:
        cipher= raw_input('Masukkan pesan\t: ')
        print(dekrip(cipher))
        decrypt[dekrip(cipher)]=cipher
    elif pilihan == 3:
	    print encrypt
    elif pilihan == 4:
	    print decrypt
    else:
        print('Pilihan Salah!')
        break
