"""
girdi=input("Lütfen bir değer giriniz : ")
print(girdi)
"""

"""
Boolean yapısı
True
False
"""

print(1==1) #True

a="ahmet" #[a,h,m,e,t]
b="Ahmet" #[A,h,m,e,t]
print(a==b) #false a ve b yi ddizi olarak görür
print(a[1:]==b[1:]) #dizinin ilk elemanından sonrasına bakar ve True döndürür
print(a[0:]==b[0:]) #False
print(a[1:]!=b[1:]) #False

x=3
y=0
print("x<y : ", x<y) #False

c=2
d=2
if(c==d):
    print("c d ye eşittir")
print("if'e dahil değil")


#*****************************************************************************

girdi=input("Lütfen bir değer giriniz : ")

if(girdi=="Ahmet"):
    print("Doğrudur")
elif(girdi=="Mehmet"):
    print("Öğrencinin adı",girdi)
else:
    print(girdi,"diye bir öğrenci yok")

