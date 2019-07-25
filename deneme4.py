"""

==  ------> eşitse
!=  ------> eşit değilse
>   ------> büyükse
<   ------> küçükse
>=  ------> büyük eşitse
<=  ------> küçük eşitse

"""

giris = input("paralo: ")

sifre = "deneme"

# if giris != sifre:
#     print("paralo yanlış")


giris = input("10 ie 100 arasında sayı girin")

giris = int(giris)

if giris > 50:
    print("50'den büyük")
elif giris < 50:
    print("50'den küçük")
else:
    print("sayı 50")

