herbivora = {'Jerapah','Kuda','Onta','Kanguru','Angsa',\
             'Anoa','Burung Merpati','Kelelawar'}
karnivora = {'Musang','Singa','Beruang','Bangau',\
             'Burung Hantu','Penguin','Burung Pelatuk'}
kaki4 = {'Jerapah','Kuda','Anoa','Onta','Musang','Singa',\
         'Beruang'}
kaki2 = {'Kanguru','Angsa','Burung Merpati','Kelelawar',\
         'Bangau','Burung Hantu','Penguin','Burung Pelatuk'}

def a():
    print 'Omnivora : '
    print (karnivora&kaki2)

def b():
    print 'Karnivora Berkaki 2'
    print (karnivora&kaki2)
b()
