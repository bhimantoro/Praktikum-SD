'''
angka = [x**2 for x in range(1,20)]
print "list bilangan pangkat dua antara bilangan 1 dan 20"
print angka[0:5], "5 elemen pertama"
angka.reverse()
print angka[0:5], "5 elemen terakhir"
'''

angka = [x**2 for x in range(1,20)]
angka = [x for x in angka if x < 20]
print "list pangkat dua  =>", angka
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "5 elemen pertama  =>", angka[:5]
print "5 elemen terakhir =>", angka[-5:]
