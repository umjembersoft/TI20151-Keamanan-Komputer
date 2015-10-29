import hashlib
print
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print("Program Sederhana phyton")
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print
NamaString = "Wahyu Hari"

hash = hashlib.sha384()
hash.update(NamaString)
hexSHA256 = hash.hexdigest()

print("Nilai hash SHA 384 dari String " +NamaString+ " adalah : " + hexSHA256.upper())
print
print("Penghitungan Nilai Hash Selesai")