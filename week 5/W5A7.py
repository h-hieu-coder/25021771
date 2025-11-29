a,dau,b = map(str, input().split())
def solve(a,dau,b): 
    if dau == "*" : 
        return float(a)*float(b) 
    elif dau =="/" :
        return float(a)/float(b)
    elif dau == "+" : 
        return float(a)+float(b)
    elif dau == "-" : 
        return float(a)-float(b)
print(round(solve(a,dau,b),2))