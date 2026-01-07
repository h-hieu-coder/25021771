class Fraction : 
    def __init__(self, num, den ) : 
        self.num = num 
        self.den = den 

    def __str__(self) : 
        a = self.num 
        b = self.den
        while self.den != 0 : 
            self.num ,self.den = self.den ,self.num % self.den 
        ucln = self.num 
    
        return f"{a//ucln}/{b//ucln}"
    
a, b, op, c, d = map(str, input().split())
a, b, c, d = int(a), int(b), int(c), int(d)

if op == "+" : 
    add = Fraction(a*d + b*c,b*d)
    print(add.__str__())

elif op == "-" : 
    subtract = Fraction(a*d - b*c , b*d) 
    print(subtract.__str__()) 

elif op == "*" : 
    mul = Fraction(a*c , b*d) 
    print(mul.__str__())

elif op == "/" : 
    divice = Fraction(a*d, b*c) 
    print(divice.__str__())

else : 
    print("ERROR")