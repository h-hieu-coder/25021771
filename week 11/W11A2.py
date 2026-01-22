my_list = list(map(int, input().split()))
n = len(my_list)
try : 
    print(my_list[n])
except IndexError : 
    print("Phan tu khong ton tai")