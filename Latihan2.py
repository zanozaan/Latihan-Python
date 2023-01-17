print("LATIHAN 2")
##1. ----0++++++5------8++++++11----
##2. ++++0------5++++++8------11++++

inputan = float(input("masukan angka yang bernilai\nkurang dari 0\nkurang dari 8: "))

##----0+++++
inputanA = inputan > 0

##+++++5-----
inputanB = inputan < 5

##---8++++
inputanC = inputan > 8

##++++11-----
inputanD = inputan < 11

##----0++++++5------8++++++11----
nilaiC = inputanA and inputanB or inputanC and inputanD
print("angka yang anda masukkan: ", nilaiC)

print("\n",20*'=',"\n")
print("LATIHAN 2")
inputan = float(input("masukan angka yang bernilai\nkurang dari 5\nkurang dari 11: "))

##+++++0----
inputanA = inputan < 0

##-----5+++++
inputanB = inputan > 5

##++++8---
inputanC = inputan < 8

##-----11++++
inputanD = inputan > 11

##+++++++0-----5+++++8------11++++++
nilaiC = inputanA or inputanB and inputanC or inputanD
print("angka yang anda masukkan: ", nilaiC)