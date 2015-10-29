__author__ = 'Biggy_1310651066'

import hashlib

print
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print("Program Sederhana Untuk Melakukan Generate Terhadap Nilai Hash dari MD5")
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print

NamaString = "Biggy ramadhanies"

hash = hashlib.sha384()

hash.update(NamaString)

hexsha384 = hash.hexdigest()

print("Nilai hash md5 dari String " +NamaString+ " adalah : " + hexsha384.upper())

print

print("Penghitungan Nilai Hash Selesai")


 

