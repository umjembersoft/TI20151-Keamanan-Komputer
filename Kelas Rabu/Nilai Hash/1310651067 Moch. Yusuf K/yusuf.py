__author__ = 'yusuf'

import hashlib

print
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print("Program Sederhana Untuk Melakukan Generate Terhadap Nilai Hash dari SHA 256")
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print

NamaString = "1310651067_M_Yusuf_k" #berisi variable nama dan nim

hash = hashlib.md5() #perintah hash ke MD5

hash.update(NamaString)

hexSHA256 = hash.hexdigest()

print("Nilai hash SHA 256 dari String " +NamaString+ " adalah : " + hexSHA256.upper())

print

print("Penghitungan Nilai Hash Selesai")
