print("Kalkulator Sederhana")
print("="*20)

angka1 = float(input("angka pertama: "))
operasi = input("Masukkan operasi yang ingin anda proses : ")
angka2 = float(input("angka kedua :"))

if operasi == "+":
    penjumlahan = angka1 + angka2
    print("Hasil: ", penjumlahan)
    
elif operasi == "-":
    pengurangan = angka1 - angka2
    print("Hasil: ", pengurangan)
    
elif operasi == "*":
    perkalian = angka1 * angka2
    print("Hasil: ", perkalian)
    
elif operasi == "/":
    pembagian = angka1 / angka2
    print("Hasil: ", pembagian)
