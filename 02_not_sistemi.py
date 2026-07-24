not1 = int(input("Öğrencinin ilk  yazılı notunu giriniz: "))
not2 = int(input("Öğrencinin ikinci yazılı notunu giriniz: "))
not3 = int(input("Öğrencinin sözlü notunu giriniz: "))
ortalama = (not1+not2+not3)/3
print((f"Ortalamanız : {ortalama}"))
if ortalama <= 24:
    print(("Notunuz: 0"))
elif ortalama >= 25 and ortalama <= 44:
    print(("Notunuz: 1"))
elif ortalama >= 45 and ortalama <= 54:
    print(("Notunuz: 2"))
elif ortalama >= 55 and ortalama <= 69:
    print(("Notunuz: 3"))
elif ortalama >= 70 and ortalama <= 84:
    print(("Notunuz: 4"))
else:
    print(("Notunuz: 5"))
