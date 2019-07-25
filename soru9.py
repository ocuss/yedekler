#iki adet 1 ile 7 arasında sayı üreticeksin eğer sayılar aynıysa kazandıznız yazısı cıkıcak.
import random
sayi1 = random.randint(1,7)
sayi2 = random.randint(1,7)

def zar(sayi1,sayi2):
    if sayi1 == sayi2:
        return "oyunu kazandınız."
    else:
        return "tekrar deneyiniz."
print(zar(sayi1,sayi2))
