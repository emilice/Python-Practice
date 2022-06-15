#Fonksiyonlar
"""
f(x)=y
x: girdi
y: çıktı
x, y çağrılmadan çalışmaz
def: defination(tanım)
"""

#fonk. tanımlama
def ornek_fonk(): 
    print("merhaba")
ornek_fonk() #fonk. çağırma çıktısı merhaba olur

#**********************************************************************

x=5 #fonksiyon içindeki x ve fonksiyon içindeki x farklıdır
def ornek1(x): 
    print("ornek1:",x)
ornek1("ahmet") #x=ahmet'tir
ornek1("memet")

#**********************************************************************

def ornek2(x,y):
    print("ornek2:", x)
    print("ornek2:",x,y)
ornek2("mehmet", "ahmet")

#**********************************************************************

def ornek3(x="mehmet",y="ahmet"):
    print("ornek3:",x,y)
ornek3() #x,y'ye hangi değerler(default değer alınır) verildiyse o değer çıktı olarak alınır
ornek3("mehmet", "ahmet") #çağrılan fonksiyon içine verilen değerler önceliklidir, onlar çıktı olarak alınır

def ornek4(x,y="ahmet"):
    print("ornek4:",x,y)
ornek4("mehmet")

def ornek5(y, x="ahmet"): #x,y sırasında uyarı verir, bu nedenle y baştadır
    print("ornek5:",x,y)
ornek5("mehmet")

def ornek6(x):
    for i in x:
        print("ornek6:",i)
ornek6("mehmet")
#Çıktı: m,e,h,m,e,t
ornek6([1,2,3])
#Çıktı: 1,2,3


def ornek7(x):
    for i in range (len(x)):
        print("ornek7:",i)
ornek7("mehmet")
#Çıktı: 0,1,2,3,4,5
ornek7([1,2,3])
#Çıktı: 0,1,2


#********************************************************************

def toplam(x):
    _toplam=0
    for i in x:
        _toplam+=i
    return _toplam
#toplam([1,2,3,4]) bu fonksiyon sadece bir veri döndürür
a=toplam([1,2,3,4]) #toplam sonucu bir integer döndü ve a'ya atandı
print("toplam sonuç:",str(a))
#a'yı integer, çıktıda string yazdırmaya çalışıldığından str(a) kullanıldı
#a olarak yazıldığında TypeError hatası verir
print("toplam sonuç2:",str(toplam([1,2,3,4])))

#*******************************************************************

def ornek8(name1, name2, name3):
    print("ornek8:",name1)
ornek8(name1="a", name2="b",name3="c") #a
ornek8("d","b","c") #d

def ornek9(*name1):
    print("ornek9:",name1[2])
ornek9("d","b","c") #c name1'e dizinin 2. elemanı çıktı olarak verilir

#**********************************************************************

def ornek10(*name1):
    pass
ornek10("isim") #çıktı olarak bir şey üretmez, pass yazılmazsa hata verir





