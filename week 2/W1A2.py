#Bai 2 Tính phần diện tích còn lại để trồng cây
a,b = map(int,input().split()) #a : rong , b: dai
pi = 3.14
S_hcn = a*b
r = a/2
S_ht = pi* r**2
S = S_hcn - S_ht
print(round(S,2))