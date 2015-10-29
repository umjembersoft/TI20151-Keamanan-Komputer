__author__ = 'candra'

import hashlib

print
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print("Program Sederhana Untuk Melakukan Generate Terhadap Nilai Hash dari MD 5")
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print

NamaString = "candara"

hash = hashlib.md5()

hash.update(NamaString)

hexMD5 = hash.hexdigest()

print("Nilai hash MD 5 dari String " +NamaString+ " adalah : " + hexMD5.upper())

print

print("Penghitungan Nilai Hash Selesai")
