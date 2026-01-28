#W9A9
def Median(nums):
    a,b,c,d,e = nums
    if a > b:
        a,b=b,a
    if c>d:
        c,d=d,c
    if a>c:
        a,c=c,a
        b,d=d,b
    if e < b:
        return b
    if e > c:
        return c
    return e
nums = list(map(int,input().split()))
print(Median(nums))