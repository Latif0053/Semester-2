# Soal No.4
mahasiswa = {
    "2351345TK22456": "Fahim",
    "2467890KG25467": "Edelweis",
    "2245644SV23478": "Muhammad Hardiyanto"
}
a = input("Masukkan NIM (tanpa garing): ")
if a in mahasiswa:
    print(mahasiswa[a])
else:
    print("Mohon maaf, data kamu belum tersedia.")
