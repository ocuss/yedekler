karakter1 = {"isim":"süperman",
            "güç" :120,
            "yetenek":"uçmak",
            "can":500} 
print("karakterin_adi      : {}".format(karakter1["isim"]))
print("karakterin_gücü     : {}".format(karakter1["güç"]))
print("karakterin_yeteneği : {}".format(karakter1["yetenek"]))

karakter2 = {"isim":"hulk",
             "güç":210,
             "yetenek":"dönüşüm",
             "can":900}
print("karakterin_adi      : {}".format(karakter2["isim"]))
print("karakterin_gücü     : {}".format(karakter2["güç"]))
print("karakterin_yeteneği : {}".format(karakter2["yetenek"]))

def vur(vuran:dict,vurulan:dict):
    eksilen = vuran["güç"]
    vurulan["can"] = vurulan["can"] - eksilen
vur(karakter1,karakter2)
vur(karakter2,karakter1)
print("karakter1 can:",karakter1["can"])
print("karakter2 can:",karakter2["can"])
