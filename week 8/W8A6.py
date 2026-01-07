class Retangle : 
    def __init__(self, wide, high):
        self.wide = wide
        self.high = high

    def area(self) : 
        print('%.2f'%(self.wide*self.high), end = " ")
    
    def perimeter(self) : 
        print('%.2f'%(2*self.wide + 2*self.high))

w, h, k = map(float, input().split())

chu_nhat = Retangle(w*k ,h*k) 
chu_nhat.area()
chu_nhat.perimeter()