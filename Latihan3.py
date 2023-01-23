import datetime as dt
hari_ini = dt.date.today()

print("\n"+5*"="+"Input Tanggal Lahir"+5*"=")
print("Masukkan tanggal lahir anda")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal) 

hari_ini = dt.date.today()
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365) // 30
umur_tanggal = (umur_hari.days % 30)
print(f"\nTanggal lahir anda adalah : {tanggal_lahir}")
print(f"Hari nya adalah : {tanggal_lahir:%A}")
print(f"Umur anda adalah: {umur_tahun} tahun, {umur_bulan} bulan, {umur_tanggal} hari")