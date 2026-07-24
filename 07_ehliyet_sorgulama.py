ad = input("Adınızı Giriniz: ")
yas = int(input("Yaşınızı Giriniz: "))
egitim = int(input("""
1- ilkokul
2- Ortaokul
3- Lise
4- Üniversite
En güncel mezuniyetinizi seçiniz: """))

if yas >=18:
    if egitim == 3 or egitim == 4:
        print(f"{ad} kişisi ehliyet alabilir.")
    else:
        print(f"{ad} kişisi eğitim yetersizliğinden ehliyet alamaz.")
else:
    print(f"{ad} kişisi yaşı yetmediği için ehliyet alamaz.")
