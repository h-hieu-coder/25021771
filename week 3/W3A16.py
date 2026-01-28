# lam tron len
def lam_tron_len(x):
    nguyen = int(x)
    if x > 0 and x != nguyen:
        return nguyen + 1
    else:
        return nguyen

# lam tron xuong
def lam_tron_xuong(x):
    nguyen = int(x)
    if x < 0 and x != nguyen:
        return nguyen - 1
    else:
        return nguyen

# lam tron
def lam_tron(x):
    nguyen = int(x)
    thap_phan = abs(x-nguyen)
    if x>=0 :
        if thap_phan >=0.5:
            return nguyen +1
        else :
            return nguyen
    else :
        if thap_phan >= 0.5:
            return nguyen -1
        else :
            return nguyen

n = float(input())
print(lam_tron_len(n),lam_tron_xuong(n), lam_tron(n),sep=" ")