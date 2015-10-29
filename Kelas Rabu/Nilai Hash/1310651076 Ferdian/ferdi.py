__author__ = 'ferdian'

import hashlib

print
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print("Program Sederhana Untuk Melakukan Generate Terhadap Nilai Hash dari sha512")
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print

NamaString = "ferdian akbar"

hash = hashlib.sha512()

hash.update(NamaString)

hexSHA512 = hash.hexdigest()

print("Nilai hash MD 5 dari String " +NamaString+ " adalah : " + hexSHA512.upper())

print

print("Penghitungan Nilai Hash Selesai")
