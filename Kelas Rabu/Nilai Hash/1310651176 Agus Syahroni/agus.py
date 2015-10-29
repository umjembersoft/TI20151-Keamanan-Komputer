

import hashlib

print
print ("Nim : 1310651176")
print ("Nama : agus syahroni")
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("Program Sederhana Untuk Melakukan Generate Terhadap Nilai Hash dari SHA 384")
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print

NamaString = "agus"

hash = hashlib.sha512()

hexSHA256 = hash.hexdigest()

print("Nilai String Dari " +NamaString+ " adalah : " + hexSHA256.upper())

print

print("Penghitungan Nilai Hash Selesai")
