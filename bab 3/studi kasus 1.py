Andi = {'BD','PBO','KDJK','PW'}
Budi = {'BD','KDJK'}
Sinta = {'SD','TI','KDJK'}
Union = (Andi|Budi|Sinta)

def line_break():
    print '\n'*15

def soal_a():
    line_break()
    print 'matakuliah yang diambil ketiga mahasiswa'
    print ', '.join(Union)

def soal_b():
    line_break()
    print 'matakuliah yang sama antara mereka bertiga'
    print ', '.join(Andi&Budi&Sinta)

def soal_c():
    line_break()
    print 'matakuliah yang tidak diambil antara 2 mahasiswa'
    print ', '.join((Andi|Budi)^Union), \
        '(Andi dan Budi)'
    print ', '.join((Budi|Sinta)^Union), \
        '(Budi dan Sinta)'
    print ', '.join((Andi|Sinta)^Union), \
        '(Andi dan Sinta)'

def soal_d():
    line_break()
    print 'matakuliah yang sama-sama diambil antara 2 mahasiswa'
    print ', '.join((Andi&Budi)&Union), \
        '(Andi dan Budi)'
    print ', '.join((Budi&Sinta)&Union), \
        '(Budi dan Sinta)'
    print ', '.join((Andi&Sinta)&Union), \
        '(Andi dan Sinta)'

def menu():
    while True:
        pil = str(raw_input('Masukkan pilihan (a/b/c/d): '))
        if pil == 'a':
            soal_a()
        elif pil == 'b':
            soal_b()
        elif pil == 'c':
            soal_c()
        elif pil == 'd':
            soal_d()
        else:
            line_break()
            print 'Salah bossqu'
            break

menu()
