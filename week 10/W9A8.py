#W9A8
path = {'R':[0,1],'L':[0,-1],'U':[-1,0],'D':[1,0]}
a={(0,0)}
def is_path_crossing(moves):
    i,j = 0,0
    for ch in moves:
        i1 = i + path[ch][0]
        j1 = j + path[ch][1]
        if (i1,j1) in a:
            return True
        a.add((i1,j1))
        i,j = i1,j1
    return False
moves = input()
if is_path_crossing(moves):
    print('True')
else:
    print('False')