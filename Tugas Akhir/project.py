import string
import os

alfabet = string.printable
# string printable mencakup letters, punctuations, digits dan whitespace
# dengan total 100 karakter, yang digunakan sebagai modulus

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
            k = (k - 3)%100
            pesan = pesan+alfabet[k]
        else:
            pesan = pesan + i

    return pesan

encrypt = {} #init dictionary enkripsi
decrypt = {} #init dictionary dekripsi

def pause():
	os.system('pause')

while True:
	try:
	    print('-----------------------------\n'
	          '|     Copyright (c) 2018    |\n'
	          '|   Austin Fascal Iskandar  |\n'
	          '|  Bhimantoro Suryo Admodjo |\n'
	          '|     Kamus CaesarCipher    |\n'
	          '-----------------------------')
	    pilihan = int(raw_input('1. Enkripsi\n'
	                            '2. Dekripsi\n'
	                            '3. Tampil Kamus\n'
	                            '----------------------------\n'
	                            'Pilih Menu\t: '))
	    if pilihan == 1:
	        pesan = raw_input('Masukkan pesan\t: ')
	        print(enkrip(pesan))
	        pause()
	        encrypt[pesan]=enkrip(pesan)
	    elif pilihan == 2:
	        cipher= raw_input('Masukkan pesan\t: ')
	        print(dekrip(cipher))
	        decrypt[cipher]=dekrip(cipher)
	        pause()
	    elif pilihan == 3:
		    print 'Kamus Enkripsi\n', \
		          encrypt, \
		          '\nKamus Dekripsi\n', \
		          decrypt
		    pause()
	    else:
	        break
	except ValueError:
		print 'Oops! Pilihan salah. Coba lagi...'
