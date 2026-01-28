#W9A10
def findRadius(houses,heaters):
    houses.sort()
    heaters.sort()
    i = 0
    r = 0
    for h in houses:
        while i < len(heaters) -1 and abs(heaters[i+1]-h) <= abs(heaters[i]-h):
            i+=1
        r = max(r,abs(heaters[i] - h))
    return r
houses = list(map(int,input().split()))
heaters = list(map(int,input().split()))
print(findRadius(houses,heaters))