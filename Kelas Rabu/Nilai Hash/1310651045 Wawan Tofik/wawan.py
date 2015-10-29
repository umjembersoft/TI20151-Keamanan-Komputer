

import hashlib

print
print ("Nim : 1310651045")
print ("Nama : Wawan Tofik")
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("Program Sederhana Untuk Melakukan Generate Terhadap Nilai Hash dari SHA 384")
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print

NamaString = "Wawan"

hash = hashlib.sha384()

hexSHA256 = hash.hexdigest()

print("Nilai String Dari " +NamaString+ " adalah : " + hexSHA256.upper())

print

print("Penghitungan Nilai Hash Selesai")
