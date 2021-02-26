#membuat gabungan dari rentan angka
#+++3------10+++

inputUser = float(input("masukkan angka yg bernilai kurang dari 3 : "))

#memriksa nilai kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 = ", isKurangDari)

#memeriksa nilai lebih dari 3
isLebihDari = (inputUser > 3)
print("Lebih dari 3 = ", isLebihDari)

isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukkan ", isCorrect)

#irisan
#----3+++++10-----