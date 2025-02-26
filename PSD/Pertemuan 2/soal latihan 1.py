# Soal No.1
data = input("masukkan 5 angka(dipisahkan dengan spasi): ")
a=list(map(int,data.split()))
print("Data yang di input: ",a)
b=sorted(a)
print("Data yang sudah terurut" , b )
print("Jumlah semua data", sum (a)) 
b.pop() 
print(b)
