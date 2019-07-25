import random
sayi = random.randint(1,10)
while True:
    i = int(input("bir sayı giriniz:  "))
    print(i)
    if i == sayi:
        print("sayı doğrudur.")
        break
    elif i > sayi:
        print("sayıyı azalt.")
    elif i < sayi:
        print("sayıyı artır.")
        
        
        

