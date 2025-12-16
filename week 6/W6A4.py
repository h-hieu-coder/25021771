s = input().split()
d = {}
for pair in s:
    key, value = pair.split(":")

    if key not in d:
        d[key] = [value]
    else:
        d[key].append(value)

print(d)
