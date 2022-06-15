#en küçük değeri bulan fonksiyon

def find_min(liste):
    min=liste[0] #min listenin ilk elemanına eşit
    for i in range (len(liste)): #liste uzunluğu kadar döngü dönecek
        print(i)
        if(liste[i]<min):
            min=liste[i]
    return min
print("listenin en küçük elemanı: ", find_min([10,15,5,9,-2,17,12]))


#Daha hızlı çalışması için aşağıdaki gibi yazılmalı, fazladan bir işlem atılır

def find_min1(liste):
    min=liste[0] #min listenin ilk elemanına eşit
    for i in range (len(liste)-1): #liste uzunluğu kadar döngü dönecek
        print(i)
        if(liste[i+1]<min):
            min=liste[i+1]
    return min
print("listenin en küçük elemanı: ", find_min1([10,15,5,9,-2,17,-3]))



#En büyük değeri bulan fonksiyon******************************************

def find_max(liste):
    max=liste[0]
    for i in range (len(liste)-1):
        if(liste[i+1]>max):
            max=liste[i+1]
    return max
print("lstenin en büyük elemanı:",find_max([3,4,9,5,1]))
    
