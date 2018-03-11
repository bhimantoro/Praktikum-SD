herbivora = {'jerapah','kuda','onta','kanguru','angsa',\
             'anoa','burung merpati','kelelawar','ayam',\
             'bebek','beruang','musang','babi','tupai'}
karnivora = {'musang','singa','beruang','bangau',\
             'burung hantu','penguin','burung pelatuk','ayam',\
             'bebek','babi','tupai'}
kaki4 = {'jerapah','kuda','anoa','onta','musang','singa',\
         'beruang','babi','tupai'}
kaki2 = {'kanguru','angsa','burung merpati','kelelawar',\
         'bangau','burung hantu','penguin','burung pelatuk',\
         'ayam','bebek'}

omni = karnivora&herbivora

def omnivora():
    print 'Omnivora : \n', \
          ', '.join(omni)

def karnivora2():
    print 'Karnivora Berkaki 2\n', \
          ', '.join(karnivora&kaki2)

def karnivora4():
    print 'Karnivora Berkaki 4\n', \
          ', '.join(karnivora&kaki4)

def herbivora2():
    print 'Herbivora Berkaki 2\n', \
          ', '.join(herbivora&kaki2)

def herbivora4():
    print 'Herbivora Berkaki 4\n', \
          ', '.join(herbivora&kaki4)

def omnivora2():
    print 'Omnivora Berkaki 2\n', \
          ', '.join(omni&kaki2)

def omnivora4():
    print 'Omnivora Berkaki 4\n', \
          ', '.join(omni&kaki4)

def line_break():
    print '\n'*5

def menu():
    while True:
        print '==============================\n' \
              'Kebun Binatang Madagascar\n' \
              'a.\tHewan Omnivora\n' \
              'b.\tHewan Karnivora Berkaki 2\n' \
              'c.\tHewan Karnivora Berkaki 4\n' \
              'd.\tHewan Herbivora Berkaki 2\n' \
              'e.\tHewan Herbivora Berkaki 4\n' \
              'f.\tHewan Omnivora Berkaki 2\n' \
              'g.\tHewan Omnivora Berkaki 4\n'
        pil = raw_input('Masukkan Menu Pilihan : ')
        if pil == 'a':
          line_break()
          omnivora()
        elif pil == 'b':
          line_break()
          karnivora2()
        elif pil == 'c':
          line_break()
          karnivora4()
        elif pil == 'd':
          line_break()
          herbivora2()
        elif pil == 'e':
          line_break()
          herbivora4()
        elif pil == 'f':
          line_break()
          omnivora2()
        elif pil == 'g':
          line_break()
          omnivora4()
        else:
          line_break()
          print 'Salah Menu Babanq'
          break

menu()      

