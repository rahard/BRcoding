
# membaca berkas ASCII 
# 1. ambil 2 karakter
# 2. konversikan ke biner
# 3. simpan ke berkas

file = open("berkasascii.dat", "r")
#file = open("8080.txt", "r")
newfile = open("keluaran.bin", "wb")

data = file.read(2)
while data:
   # print(data)
   x = bytes.fromhex(data)
   newfile.write(x)
   data = file.read(2)
