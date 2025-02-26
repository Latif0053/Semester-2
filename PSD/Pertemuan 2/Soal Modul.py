# Soal modul mk 2.1
datamahasiswa = {}

def masuk():
    print("Silahkan input data berikut: ")
    nama = input("Nama: ")
    nim = input("NIM: ")
    daerah = input("Asal: ")
    tali = input("Tanggal lahir (dd/mm/yyyy): ")
    datamahasiswa[nim] = [nama, daerah, tali]
    print("Data berhasil ditambahkan!\n")
def secure():
    print("Mohon maaf, fitur masih dalam pengembangan.\n")
def cetak():
    if not datamahasiswa:
        print("Belum ada data mahasiswa.\n")
        return
    print("Data Mahasiswa:")
    for key, na in datamahasiswa.items():
        print(f"""Nama : {na[0]}
NIM : {key}
Daerah : {na[1]}
Tanggal Lahir : {na[2]}\n""")

def hapus():
    print("Masukkan NIM dari mahasiswa yang ingin dihapus:")
    noim = input()
    if noim in datamahasiswa:
        del datamahasiswa[noim]
        print("Data berhasil dihapus!\n")
    else:
        print("NIM tidak ditemukan!\n")
def yesno():
    while True:
        a = input().lower()
        if a in ["y", "n"]:
            return a
        else:
            print("Input tidak valid! Masukkan 'y' atau 'n'.")

while True:
    print("""Selamat datang..!!
Menu:
1. Input Data
2. Tampilkan Data
3. Hapus Data
4. Exit
""")
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        masuk()
        print("Apakah Anda ingin mengamankan data Anda? (y/n) :")
        a = yesno()
        if a == "y":
            secure()
        print("Kembali ke Menu.")
    elif pilihan == "2":
        cetak()
    elif pilihan == "3":
        hapus()
    elif pilihan == "4":
        print("Apakah Anda yakin ingin keluar? (y/n): ")
        a = yesno()
        if a == "y":
            print("Terima kasih! Program selesai.")
            break
        print("Kembali ke Menu.")
    else:
        print("Pilihan tidak valid! Silakan masukkan angka 1-4.\n")
