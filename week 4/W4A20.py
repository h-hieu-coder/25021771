n = int(input())
if n&(n-1) == 0 :
    print("YES")
else : 
    print("NO")
"""
 2^k trong he nhi phan co dang 100...0
 2^k-1 co dang                 011...1
 ma : 1&1 = 1 ; 1&0 = 0 ; 0&1 = 0
 nen n*(n-1) = 0 neu n = 2^k
"""