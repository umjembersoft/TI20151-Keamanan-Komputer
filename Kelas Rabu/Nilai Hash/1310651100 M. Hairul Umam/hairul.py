__author__ = 'Fatmawatiningsih_1310651047'

import hashlib

print
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print("Program Sederhana Untuk Melakukan Generate Terhadap Nilai Hash dari MD5")
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print

NamaString = "Fatmawatiningsih"

hash = hashlib.sha1()

hash.update(NamaString)

hexsha1 = hash.hexdigest()

print("Nilai hash md5 dari String " +NamaString+ " adalah : " + hexsha1.upper())

print

print("Penghitungan Nilai Hash Selesai")


 

