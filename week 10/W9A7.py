#W9A7
def canplaceflower(flower,k):
    
    flower = [0] + flower + [0]
    n = len(flower)
    for i in range(1,n-1):
        if flower[i] == 0 and flower[i+1] == 0 and flower[i-1] == 0:
            k -= 1
            flower[i] = 1
    return k <= 0
flower = list(map(int,input().split()))
k = int(input())
print('True' if canplaceflower(flower,k) else "False")