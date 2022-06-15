#while, for döngüsü

i=1
while (i<6):
    print("i : ",i)
    i+=1 #i'nin artması amaçlanmakta, i 6 olduğunda while döngüsünden çıkar
#Çıktı 1,2,3,4,5

#**************************************************************************
  
a=1  
while (True):
    print("a : ",a) 
    a+=1 
    if(a==6): 
        break
#Çıktı: 1,2,3,4,5

#**************************************************************************


b=1  
while (True):
    b+=1 
    if(b==6): 
        continue #6 değerini eşitse o adımı atlar, işlem devam etmez, 7'ye geçer
    print("b : ",b)
    if(b==10):
        break #10 değerine eşitse b döngüden çıkar
#Çıktı : 2,3,4,5,7,8,9,10

#**************************************************************************


c=1
while (c<6):
    c+=1
    if(c==3):
        continue
    print(c)
else:
    print("done")
    
#Çıktı : 2,4,5,6,done  

