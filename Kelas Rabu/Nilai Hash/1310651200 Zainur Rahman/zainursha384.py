__author__ = 'zainur'

import hashlib

print
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print("Program Sederhana Untuk Melakukan Generate Terhadap Nilai Hash dari sha384")
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print

NamaString = "Zainur Rahman"

hash = hashlib.sha384()

hash.update(NamaString)

hexsha384 = hash.hexdigest()

print("Nilai hash md5 dari String " +NamaString+ " adalah : " + hexsha384.upper())

print

print("Penghitungan Nilai Hash Selesai")
