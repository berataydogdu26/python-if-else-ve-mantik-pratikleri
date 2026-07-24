ad = input("Adınızı Giriniz: ")
boy= int(input("Boyunuzu Giriniz: "))
kilo= int(input("Kilonuzu Giriniz: "))
index = kilo / ((boy/100)**2)
print(f"{ad} kişisinin Kilo indexi: {index}")

if index <= 18.4:
    print("Bu ölçülere göre zayıfsınız.")
elif 18.5 <= index <= 24.9:
    print("Bu ölçülere göre normalsiniz.")
elif 25.0 <= index <= 29.9:
    print("Bu ölçülere göre fazla kilolusunuz.")
elif 30.0 <= index <= 34.9:
    print("Bu ölçülere göre şişmansınız(obezsiniz).")
