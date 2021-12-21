
# membaca berkas biner byte-per-byte
# kemudian melakukan konversi ke bentuk ASCII dari 
# nilai hexadecimal data tersebut
# (cc) 2021 Budi Rahardjo

import binascii

file = open("berkasbiner.bin", "rb")
#file = open("8080.jpeg", "rb")
byte = file.read(1)
while byte:
   #print(byte, ord(byte), hex(ord(byte)))
   x = binascii.hexlify(byte)
   y = str(x,'ascii')
   print(y, end="")
   byte = file.read(1)
