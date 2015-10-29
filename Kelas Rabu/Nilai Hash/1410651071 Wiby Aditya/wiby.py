import hashlib
print
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print("Program Sederhana phyton")
print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"
print
NamaString = "Wibi Aditya"

hash = hashlib.sha1()
hash.update(NamaString)
hexSHA256 = hash.hexdigest()

print("Nilai hash SHA 256 dari String " +NamaString+ " adalah : " + hexSHA256.upper())
print
print("Penghitungan Nilai Hash Selesai")