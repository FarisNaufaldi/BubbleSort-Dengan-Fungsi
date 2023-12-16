def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0 , n-1):
            print("i", i)
            print("j", j)
            print("j+1", j+1)
            print(arr)
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                print(arr)
Jumlah_Bilangan_Dalam_Barisan = int(input("Masukkan kalian ada ingin berapa bilangan dalam suatu barisan = "))
b = []
for i in range(Jumlah_Bilangan_Dalam_Barisan):
    a = int(input("Masukkan Bilangan untuk dimasukkan ke dalam barisan = "))
    b.append(a)
BubbleSort(b)
print(Jumlah_Bilangan_Dalam_Barisan)