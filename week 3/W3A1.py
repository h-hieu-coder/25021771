n = int(input())
def dao_nguoc(n):
    while(n>0):
        last = n%10
        print(last,end="")
        n//=10
dao_nguoc(n)