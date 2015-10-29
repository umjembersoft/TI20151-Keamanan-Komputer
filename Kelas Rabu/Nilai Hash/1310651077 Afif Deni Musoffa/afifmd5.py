__author__ = 'afif_deni_musoffa_1310651077'

import hashlib

print
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print("Program Sederhana Untuk Melakukan Generate Terhadap Nilai Hash dari md5")
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print

NamaString = "afif deni musoffa"

hash = hashlib.md5()

hash.update(NamaString)

hexmd5 = hash.hexdigest()

print("Nilai hash md5 dari String " +NamaString+ " adalah : " + hexmd5.upper())

print

print("Penghitungan Nilai Hash Selesai")
