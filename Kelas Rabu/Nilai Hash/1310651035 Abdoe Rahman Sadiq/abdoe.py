__author__ = 'Abdoe Rahman Sadiq'

import hashlib

print
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print("Program Sederhana Untuk Melakukan Generate Terhadap Nilai Hash dari MD5")
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print

NamaString = "1310651035_Abdoe Rahman Sadiq" #ini adalah variabel yang berisi nama dan nim

hash = hashlib.md5 	() #ini adalah perintah hash ke MD5, bisa kondisikan misal diganti sha256

hash.update(NamaString) 

abdu = hash.hexdigest()

print("Nilai hash SHA 256 dari String " +NamaString+ " adalah : " + abdu.upper())

print

print("Penghitungan Nilai Hash Selesai")
