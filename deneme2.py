print("""

[1] toplama işlemi
[2] çıkarma işlemi
[3] çarpma işlemi
[4] toplama işlemi
[5] üs alma
[Q] çıkış



   """)



giris = input("Seçiminiz: ")

if giris == "1":	
	x = input("ilk sayı: ")
	x = float(x)
	y = input("ikinci sayı: ")
	y = float(y)

	print("işlem sonucu: ",x + y)

if giris == "2":
	x = input("ilk sayı: ")
	x = float(x)
	y = input("ikinci sayı: ")
	y = float(y)

	print("işlem sonucu: ", x - y)

if giris == "3":
	x = input("ilk sayı: ")
	x = float(x)
	y = input("ikinci sayı: ")
	y = float(y)

	print("işlem sonucu: ", x * y)

if giris == "4":
	x = input("ilk sayı: ")
	x = float(x)
	y = input("ikinci sayı: ")
	y = float(y)

	print("işlem sonucu ", x/y)


if giris == "5":
	x = input("taban: ")
	y = input("kuvvet: ")
	
	x = float(x)
	y = int(y)


	print("işlem sonucu: ",x**y)


