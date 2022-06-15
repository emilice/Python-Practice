"""Birçok nesnemiz var ve biz bunu daha modern hale getirmek
istiyorsak sınıflar kullanılır. Basit derli toplu programlar
yazmak amaçlanıyor.

İnsanlar, hayvanlar ve bitkiler isimli sınıflarımız olacak ve
Aritmatik operatörler.PNG

self:her sınıfın özelliklerini her fonk. kullanmak isteniyorsa
veya sınıfın fonksiyonlarını başka sınıfın içinde çağırmak isteniyorsa
bu şekilde interaktif bir yapı kullanmak isteniyorsa self paramatresi kullanılır.
"""

class ornek_sınıf():
    a="Değişmez veri"
    def __init__(self): #init: yaratmak anlamında sınıf oluşturur
        print("Sınıf oluşturuldu")
        self.veri_1="örnek sınıf veri_1" #veri_1 self ile tanımlandığından sınıfın verisi oluyor
        self.veri_2="örnek sınıf veri_2"
        veri_3="örnek sınıf veri_3"

    def farkli_fonk(self):
        print("Diğer Fonksiyon")

    def veri_degistir(self):
        self.a="Değişti" #a'yı self ekleyerk sınıfın bir verisi yaptı

        
ornek_sınıf() #Sınıf oluşturuldu
sınıfımız=ornek_sınıf() #Sınıf oluşturuldu
print(sınıfımız.veri_1) #örnek sınıf veri_1
print(sınıfımız.veri_2) #örnek sınıf veri_2
#print(sınıfımız.veri_3) hata verir self kullanılmadığı için

print(sınıfımız.a) #Değişmez veri

sınıfımız.veri_degistir()#veri_degistir foonksiyonu çağrılır, a'yı  sınıfın verisi olarak aldı
print(sınıfımız.a) #Değişti

