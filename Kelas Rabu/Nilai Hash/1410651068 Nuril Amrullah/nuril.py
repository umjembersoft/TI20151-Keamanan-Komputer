import hashlib
print
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print("Program Sederhana phyton")
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print
NamaString = "Nuril Amrullah"

hash = hashlib.md5()
hash.update(NamaString)
hexSHA256 = hash.hexdigest()

print("Nilai hash md5 dari String " +NamaString+ " adalah : " + hexSHA256.upper())
print
print("Penghitungan Nilai Hash Selesai")