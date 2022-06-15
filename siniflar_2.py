class Kus():
    def __init__(self):
        print("Kuş sınıfı oluşturuldu")

    def senkimsin(self):
        print("Kuşum")

    def yuzebilirmisin(self):
        print("Hayır")

    def renginne(self):
        print("Mavi")

class Karga(Kus): #Karga Kuş(üst sınıf) sınıfında yer alır, kuş sınıfından fonk. çağırabilir
    def __init__(self):
        super().__init__()
        #bu bana karga sınıfı oluşturulurken kuşunda özelliklerini inition edilmesini sağlar
        #
        print("Karga sınıfı oluşturuldu")
        
    def sen_kimsin(self):
        print("Karga")

    def yuzebilirmisin(self):
        print("Evet")

    def kosabilirmisin(self):
        print("Evet")

    def renginne(self):
        print("Siyah")

karga=Karga()
karga.renginne()
"""
kargada bir kuştur, karga sınıfının ierisinde renginne isimli bir fonk. yoktur
Kuş sınıfında yer aldığı için kuş sınıfından renginne fonk. çağırdı

Sonradan karga sınıfına renginne isimli bir fonksiyon eklendi, bu sınıf karga içinde yer
aldığından kuş sınıfına bakılmadı

Kuş karga sınıfının üst sınıfıdır, kargada tanımlı olmayan fonk. için kuş sınıfına bakılır
"""


"""Ekran Çıktısı:
Kuş sınıfı oluşturuldu
Karga sınıfı oluşturuldu
Siyah
"""



        
