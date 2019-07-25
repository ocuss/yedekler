kitaplistesi =[]

menu = """
[1] = kitap_ekle
[2] = kitap_çıkar
[3] = kitapları_listele
[Q] = çıkış
"""
def kitapekle(kitap,liste):
    liste.append(kitap)
    print("kitap eklendi!")
    input("Ana menuye dönmek için 'enter'a basın!")

def kitapcıkar(kitap,liste):
    liste.remove(kitap)

def listele(liste):
    for i in liste:
        print("kitap_adi: {}".format(i))
    input("Ana menuye dönmek için 'enter'a basın!")

def cıkıs():
    quit()

while True:
    print(menu)
    secim = input("seciminiz:  ")

    if secim == "1":
        kitap_adi = input("kitap adi giriniz:   ")
        kitapekle(kitap_adi,kitaplistesi)

    elif secim == "2":
        kitap_adi = input("kitap adi giriniz:   ")
        kitapcıkar(kitap_adi,kitaplistesi)
    elif secim == "3":
        listele(kitaplistesi)
    elif secim == "Q" or secim == "q":
        cıkıs()
    else:
        print("hatalı girdiniz.")
        input("Ana menuye dönmek için 'enter'a basın!")
        


    
