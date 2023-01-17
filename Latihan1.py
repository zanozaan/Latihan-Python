print("LATIHAN 1")
##1. Cari nilai fahrenheit ke kelvin 
##2. Cari nilai kelvin ke fahrenheit

fahrenheit = float(input('Suhu Fahrenheit : '))
celcius = ((9/5) * fahrenheit) - 32
kelvin = celcius + 273
print("Suhu Fahrenheit adalah",kelvin, " kelvin")

kelvin = float(input('Suhu Kelvin : '))
celcius = kelvin - 273
fahrenheit= ((9/5) * celcius) + 32
print("Suhu Kelvin adalah",fahrenheit, " fahrenheit")