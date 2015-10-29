import hashlib


print ("generate nilai has")

IkiString = "fitor bogi irawan"

nilaihash=hashlib.sha512()

hexsha512=nilaihash.hexdigest()

print("nilai has SHA512 dugi String" +IkiString+ "adalah" +hexsha512.upper())

