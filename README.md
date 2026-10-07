# Mini Sefer

Mini Sefer, Python ile geliştirilmiş hibrit yapıda bir sıra tabanlı dövüş oyunudur. Oyuncu hamlelerini Tkinter tabanlı bir grafik arayüz (GUI) formu üzerinden seçerken, düşman saldırılarını savuşturmak için terminal üzerinden gerçek zamanlı refleks (QTE / Parry) mekaniği kullanır.

## Temel Özellikler

- Tkinter ile Form Girişi: input() yerine hata denetimli mini arayüz penceresi
- Gerçek Zamanlı Savunma: Terminal üzerinde kayan bar mekaniği ile zamanlama odaklı parry ve kaçış
- Rastgele Düşmanlar: Değişken can, saldırı gücü ve rastgele isimlere sahip canavarlar
- Kaynak Yönetimi: Enerji, iksir ve can dengesi üzerine kurulu stratejik hamleler

## Oyuncu Hamleleri

1. Temel Saldırı: 0 enerji harcar, düşmana 20 hasar verir.
2. Ağır Saldırı: 2 enerji harcar, düşmana 35 hasar verir.
3. İksir Kullan: 1 enerji harcar, oyuncunun canını 30 artırır (en fazla 100). Toplam 2 iksir hakkı bulunur.
4. Savunma: Enerji harcamaz, düşmandan gelecek bir sonraki hasarı yarıya indirir.

## Savunma (Parry ve Kaçış) Mekaniği

Düşman turunda terminal ekranında dolan bir çubuk belirir. Bu sırada klavyeden BOŞLUK (Space) tuşuna basma zamanlamanıza göre şu sonuçlar oluşur:

- Parry (Erken basma): Düşmanın saldırısı tamamen boşa çıkar, düşmana 20 karşı saldırı hasarı verilir ve 15 puan kazanılır.
- Kaçış (Orta zamanlama): 1 enerji harcayarak düşman saldırısından tamamen kaçılır. Enerji yetersizse hasar alınır.
- Vurulma veya Geç Kalma: Düşmanın saldırı gücüne göre tam hasar alınır. Oyuncu o tur savunma yaptıysa hasar yarıya iner.

## Sistem Gereksinimleri

- Python 3.x
- İşletim Sistemi: Windows (Koddaki gerçek zamanlı tuş algılama 'msvcrt' modülü Windows çekirdeğine özeldir)
- Ek Kütüphaneler: tkinter, random, time (Tümü Python ile hazır gelen dahili modüllerdir, harici pip kurulumu gerekmez)

