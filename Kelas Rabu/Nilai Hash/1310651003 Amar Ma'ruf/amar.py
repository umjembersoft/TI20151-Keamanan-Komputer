__author__ = 'triawan'

import hashlib

print
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print("Program Sederhana Untuk Melakukan Generate Terhadap Nilai Hash dari SHA 256")
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print

NamaString = "Amar Ma'ruf 1310651003 "

hash = hashlib.sha512()

hash.update(NamaString)

amar = hash.hexdigest()

print("Nilai hash SHA 512 dari String " +NamaString+ " adalah : " + amar.upper())

print

print("Penghitungan Nilai Hash Selesai")
