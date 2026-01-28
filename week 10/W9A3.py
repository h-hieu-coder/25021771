#W9A3
def swap_to_min(a,idx = 0):
    a = list(a)
    if idx >= len(a) - 1:
        return ''.join(a)
    target_idx = -1
    min_val = a[idx]
    for j in range(len(a) - 1,idx,-1):
        if a[j] == '0' and idx == 0:
            return swap_to_min(a,idx + 1)
        if a[j] < min_val:
            target_idx = j
            min_val = a[j]
    if target_idx != -1:
        a[idx],a[target_idx] = a[target_idx],a[idx]
        return "".join(a)
    return swap_to_min(a,idx + 1)
a = input()
print(swap_to_min(a,0))