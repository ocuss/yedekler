#klavyeden girilen 3 yazılı notunu fonksiyona gönderip ortalmasını bulan program
def ortalama(not1,not2,not3):
    sonuc = ((not1+not2+not3)/3)
    return sonuc
i = ortalama(50,85,90)
print(i)