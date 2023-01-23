print("Kalkulator Sederhana")
print("="*20)

def penjumlahan(x,y):
    return x+y

def pengurangan(x,y):
    return x-y

def perkalian(x,y):
    return x*y

def pembagian(x,y):
    return x/y

tipe= input("Masukkan angka yang ingin anda proses : ")

if tipe in ("1", "2", "3", "4", "5"):
    angka1 = float(input("angka pertama: "))
    angka2 = float(input("angka kedua :"))

if tipe == "1":
    print("Hasil: ", penjumlahan(angka1,angka2))

if tipe == "2":
    print("Hasil: ", pengurangan(angka1,angka2))

if tipe == "3":
    print("Hasil: ", perkalian(angka1,angka2))

if tipe == "4":
    print("Hasil: ", pembagian(angka1,angka2))
