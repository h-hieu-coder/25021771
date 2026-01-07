from math import sqrt

class Point : 
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    
    def check(self) :
        if self.x == 0 and self.y == 0 : 
            print("M is O\n")
        elif self.x == 0 : 
            print("M in Oy\n")
        elif self.y == 0 : 
            print("M in Ox\n")
        else : 
            print("M not in Ox or Oy")

    def distance(self) : 
        res = sqrt(self.x*self.x + self.y*self.y)
        print ('%.2f'%res) 

x, y = map(float, input().split())
point = Point(x,y) 
point.check() 
point.distance()
        