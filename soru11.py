thisdict = { 
    "car":"araba",
    "watermelon":"karpuz",
    "computer":"bilgisayar",
    "ring": "yüzük"
}
my_word = input("kelimenin anlamını öğrenmek için kelime girin:"   )


def add(my_word):
    if my_word in thisdict:
        cevap = "{0} kelimesinin anlamı: {1}"
        print(cevap.format(my_word, thisdict[word]))
    else:
        turkish = input("türkçe hali: ")
        thisdict[my_word]=turkish
while True:
    word = input("kelime gir: ")
    if word == "q":
        quit()
    else:
        add(word)
    print(thisdict)
     

   
