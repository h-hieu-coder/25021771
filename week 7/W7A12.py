lst1 = input()
lst2 = input()
lst3 = input()
lst4 = input()
mp = {} 
mp[lst1] = "A"
mp[lst2] = "B"
mp[lst3] = "C"
mp[lst4] = "D"

dp = [lst1,lst2,lst3,lst4]
def Bubble_Sort(arr) : 
    n = len(arr)
    for i in range(0,n-1) : 
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1] :
                arr[j] ,arr[j+1] = arr[j+1] , arr[j] 

Bubble_Sort(dp) 
for i in dp : 
    print(mp[i], end=" ")