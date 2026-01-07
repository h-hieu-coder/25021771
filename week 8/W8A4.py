class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def set_numbers(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def product(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            return "Error: Division by zero"
        return self.a / self.b

    def power(self):
        return self.a ** self.b

    def mod(self):
        if self.b == 0:
            return "Error: Mod by zero"
        return self.a % self.b


# ===== MAIN PROGRAM =====
a, b = map(float, input("Nhap 2 so ban dau: ").split())
calc = Calculator(a, b)

while True:
    print("""
========= CALCULATOR =========
1. Add 
2. Subtract 
3. Product 
4. Divide 
5. Power 
6. Mod 
7. Set new numbers
==============================
""")

    choice = int(input("Chon phep toan (1-7): "))

    if choice == 1:
        print("Result:", calc.add())
    elif choice == 2:
        print("Result:", calc.subtract())
    elif choice == 3:
        print("Result:", calc.product())
    elif choice == 4:
        print("Result:", calc.divide())
    elif choice == 5:
        print("Result:", calc.power())
    elif choice == 6:
        print("Result:", calc.mod())
    elif choice == 7:
        a, b = map(float, input("Nhap 2 so moi: ").split())
        calc.set_numbers(a, b)
        print("Updated numbers!")
    else:
        print("Lua chon khong hop le!")

    exit_choice = input("Ban co muon thoat? ")
    if exit_choice in ["yes", "YES", "Yes"]:
        break
