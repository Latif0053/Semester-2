# Soal No.3
namahari=("SENIN", "SELASA", "RABU", "KAMIS", "JUMAT", "SABTU", "MINGGU")

a = int(input("Masukkan angka: "))
if a <=7:
    print(namahari[a-1])
else:
    print("Kamu belum beruntung, silahkan cobalagi")
