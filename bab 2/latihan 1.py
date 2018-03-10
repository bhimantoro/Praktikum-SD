kerja = ['cleaning service','mekanik','office boy','driver','hrd','manager']
tk = ['kelapa sawit','batu bara','ojol','traveloka','asdp']
nama = raw_input('Masukkan nama anda : ')
for i in range(len(kerja)):
    print i, kerja[i]
pil = int(raw_input('Masukkan index pekerjaan : '))
for j in range(len(tk)):
    print j, tk[j]
pil2 = int(raw_input('Masukkan index perusahaan : '))
tampil = nama + " bekerja sebagai " + kerja[pil] + " di kantor " + tk[pil2]
print tampil
