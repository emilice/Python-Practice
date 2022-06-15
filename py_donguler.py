#Döngüler-----------------------------------------------------------------
"""liste=[1,2,3,4]
for i in liste:
    print("i :", i)
"""

liste=[1,2,3,4]
for i in liste:
    print("i*2 :", i*2)


liste=[1,2,3,4,5,6]
#range değeri kadar doner, listeyi döndürmez
for i in range(8):
    print("range(8) :", i)



for i in range(6):
    print("range(6) :", i*2)
print("tamamlandı")


liste=[1,2,3,4,5,6]
uretilenDizi=[0,1,2,3,4,5]
yeniDizi=[2*i for i in liste]
#yeniDizi=[2,4,6,8,10,12] olur
for i in yeniDizi:
    print("yeni dizi :", i*2)
print("tamamlandı")

#Çok boyutlu diziler-------------------------------------------------------------
cokBoyutluDizi=[1,2,3],[4,5,6],[7,8,9]
for i in cokBoyutluDizi:
    for k in i:
        print(k)
    print(i)
"""
cokBoyutluDizi=[1,2,3],[4,5,6],[7,8,9]
for i in range (len(cokBoyutluDizi)):
    print(i)
"""

cokBoyutluDizi=[1,2,3],[4,5,6],[7,8,9]
for i in range (len(cokBoyutluDizi)):
    print("Cok Boyurlu Dizi: ", cokBoyutluDizi[i])



#Sözlük ----------------------------------------------------------------
ogrenci={
    "isim":"Ahmet",
    "Başarı Notu":95,
    "Sınıf":4,
    }
ogrenci["isim"]="Mehmet"
print(ogrenci["isim"])
print(type(ogrenci["isim"])) #type ı str
print(type(ogrenci["Başarı Notu"])) #type ı int
print(type(ogrenci)) #type'ı disct yani sözlük
