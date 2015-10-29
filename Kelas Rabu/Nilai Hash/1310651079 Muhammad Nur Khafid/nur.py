

import hashlib

print
print ("Nim : 1310651079")
print ("Nama : m Muhammad nur khafid ")
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("Program Sederhana Untuk Melakukan Generate Terhadap Nilai Hash dari SHA 384")
print ("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print

NamaString = "m"

hash = hashlib.sha512()

hexSHA256 = hash.hexdigest()

print("Nilai String Dari " +NamaString+ " adalah : " + hexSHA256.upper())

print

print("Penghitungan Nilai Hash Selesai")
