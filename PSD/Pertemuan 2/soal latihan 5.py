# Soal No.5
kali = input("Ngetik kalimat random: ")
kaps= kali.upper()
vok=("A","I",'U','E','O')
no_sp = "".join(kaps.split())
j_vok={}
for i in range (len(no_sp)):
    if no_sp[i] in vok:
        if no_sp[i] in j_vok:
            j_vok[no_sp[i]] +=1
        else:
            j_vok[no_sp[i]] =1
    
    else:
        continue

# print(kaps)
# print(len(no_sp))
# print(j_vok)
print(f"""Kalimat anda:{kaps}
Jumlah huruf: {len(no_sp)}
Jumlah huruf vokal:{j_vok}
""")
