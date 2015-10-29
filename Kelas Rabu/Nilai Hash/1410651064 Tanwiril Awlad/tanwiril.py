import hashlib
print
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print("Program Sederhana phyton")
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print
NamaString = "Tanwiril Awlad"

hash = hashlib.sha224()
hash.update(NamaString)
hexSHA256 = hash.hexdigest()

print("Nilai hash SHA 224 dari String " +NamaString+ " adalah : " + hexSHA256.upper())
print
print("Penghitungan Nilai Hash Selesai")