from datetime import date

# 1. Şimdiki tarihi senin belirttiğin gibi 24 Temmuz 2026 olarak ayarlıyoruz
bugun = date(2026, 7, 24)

print("--- ARAÇ BAKIM ZAMANI HESAPLAMA ---")

# 2. Kullanıcıdan trafiğe çıkış tarihini alıyoruz
yil = int(input("Trafiğe çıkış yılını giriniz (Örn: 2018): "))
ay = int(input("Trafiğe çıkış ayını giriniz (1-12): "))
gun = int(input("Trafiğe çıkış gününü giriniz (1-31): "))

# 3. Kullanıcının girdiği bilgileri datetime nesnesine dönüştürüyoruz
trafige_cikis = date(yil, ay, gun)

# 4. İki tarih arasındaki farkı gün olarak hesaplıyoruz
fark = bugun - trafige_cikis
gecen_gun = fark.days  # Toplam geçen gün sayısı

# 5. Yıl bazlı bakım hesabı yapabilmek için günü yıla çeviriyoruz (1 yıl = 365 gün)
gecen_yil = gecen_gun // 365

# 6. Bakım durumunu kontrol ediyoruz
print("\n----------------------------------")
print(f"Araç toplamda {gecen_gun} gündür ({gecen_yil} yıl) trafikte.")

if gecen_yil < 1:
    print("Henüz 1 yıl dolmamış. Aracın 1. bakım zamanı gelmedi.")
else:
    # 1. yıl dolduysa 1. bakım, 2. yıl dolduysa 2. bakım yapılmış/zamanı gelmiştir.
    # Gelecek bir sonraki bakımı da söyleyelim:
    print(f"Aracın yapılması gereken/tamamlanan bakımı: {gecen_yil}. Bakım")
    print(f"Sıradaki bakım: {gecen_yil + 1}. Bakım")
