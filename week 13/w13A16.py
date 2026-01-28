def solve(file):
    with open(file , 'r') as f:
      a = f.read().split()
      print(a)
      i = 0
      while (i < len(a)):
         if (a[i][5] == 'S'):
            tmp , num = a[i+1].split(':')
            num = float(num)
            print(f'{num*4.0:.2f}')
            i += 2
         elif (a[i][5] == 'R'):
            tmp ,w = a[i + 1].split(':')
            tmp ,h = a[i + 2].split(':')
            w = float(w)
            h = float(h)
            print(f'{(w + h)*2.0:.2f}')
            i += 3
         else:
            tmp , r = a[i + 1].split(':')
            r = float(r)
            print(f'{2*3.14*r:.2f}')
            i += 2
file = input()
solve(file)