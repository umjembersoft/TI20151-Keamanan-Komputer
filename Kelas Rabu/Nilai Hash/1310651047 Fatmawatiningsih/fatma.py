__author__ = 'triawan'

import hashlib

print
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print("Program Sederhana Untuk Melakukan Generate Terhadap Nilai Hash dari SHA 256")
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print

NamaString = "ika martha amalia"

hash = hashlib.sha512()

hash.update(NamaString)

hexsha512 = hash.hexdigest()

print("Nilai hash SHA 256 dari String " +NamaString+ " adalah : " + hexsha512.upper())

print

print("Penghitungan Nilai Hash Selesai")
