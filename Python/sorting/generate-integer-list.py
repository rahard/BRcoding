
# membuat array integer dan kemudian diacak urutannya
# membutuhkan python 3
# 
# n adalah jumlah elemen dari array yang akan kita buat
n = 10

# buat array-nya
import array as arr
baris = arr.array('i',[])
for i in range(n):
   baris.append(i)
print(baris)

# kocok array m kali supaya isi array ditukar
m = 10
import random
for i in range(m):
   x = random.randint(0,n-1)
   y = random.randint(0,n-1)
   # swap baris(x,y)
   xi = baris[x]
   yi = baris[y]
   baris[y] = xi
   baris[x] = yi
print(baris)

# simpan di berkas
import csv
#f =open('10integer.csv', 'w', newline='')
# 'a' is for append
f =open('10integer.csv', 'a', newline='')
with f:
   writer = csv.writer(f)
   writer.writerows([baris])
