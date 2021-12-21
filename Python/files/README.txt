BR Poorman's Encoding (before BASE64)
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Konversi dari berkas BINER ke ASCII
1. python readbiner.py > berkasascii.dat
2. Lihat ukuran berkas ("berkasbiner.bin" dan "berkasascii.dat")
   Mestinya meningkat menjadi 2x lipat. Jelek dibandingkan BASE64


Kembalikan dari berkas ASCII ("berkasascii.dat") ke BINER ("keluaran.bin")
1.    python ascii2biner.py
2. hasil di "keluaran.bin"
3. periksa dengan hexadump:
      hd keluaran.bin

Hal yang sama dapat dilakukan dengan menggunakan berkas "8080.jpeg"
