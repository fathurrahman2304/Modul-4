# Nama : Fathur Rahman
# NIM : 065002200013
bulan = int(input("Masukkan Bulan: "))
tahun = int(input("Masukkan Tahun: "))
while bulan in (1,3,5,7,8,10,12):
    hari = 31
    print("\npada bulan",bulan,"terdapat",hari,"hari tahun",tahun)
    bulan += 1.5
while bulan in (4,6,9,11):
    hari2 = 30
    print("\npada bulan",bulan,"terdapat",hari2,"hari tahun",tahun)
    bulan += 1.5
while bulan == 2:
    hari3 = 28
    print("\npada bulan",bulan,"terdapat",hari3,"hari tahun",tahun)
    bulan += 1.5
if bulan < 0 or bulan > 12:
    print("\ntidak ditemukan,silahkan masukkan angka bulan pada rentang 1 sampai 12")

