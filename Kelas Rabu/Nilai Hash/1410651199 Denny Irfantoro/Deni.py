import hashlib
print
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print("Program Sederhana phyton")
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print
NamaString = "Deni Irfantoro"

hash = hashlib.sha512()
hash.update(NamaString)
hexSHA256 = hash.hexdigest()

print("Nilai hash SHA 512 dari String " +NamaString+ " adalah : " + hexSHA256.upper())
print
print("Penghitungan Nilai Hash Selesai")