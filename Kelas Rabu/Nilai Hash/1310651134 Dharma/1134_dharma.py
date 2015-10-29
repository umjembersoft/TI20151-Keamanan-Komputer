__author__ = 'Dharma Trias Brata Swasono'

import hashlib

print
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print("Program Sederhana Untuk Melakukan Generate Terhadap Nilai Hash dari MD5")
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print

NamaString = "1310651134_Dharma Trias Brata Swasono" #ini adalah variabel yang berisi nama dan nim

hash = hashlib.md5 	() #ini adalah perintah hash ke MD5

hash.update(NamaString) 

test = hash.hexdigest()

print("Nilai hash SHA 256 dari String " +NamaString+ " adalah : " + test.upper())

print

print("Penghitungan Nilai Hash Selesai")
