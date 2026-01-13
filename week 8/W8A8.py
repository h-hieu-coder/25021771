class BankAccount() : 
    def __init__(self, owner , balance):
        self.owner = owner 
        self.balance = float(balance) 

    def deposit(self, x) : 
        self.balance += x 

    def withdraw(self, x) : 
        if self.balance >= x :
            self.balance -= x 

    def __str__(self) :
        return "%.2f"% self.balance   

owner , balance = map(str, input().split())
solve = BankAccount(owner, balance) 
n = int(input()) 
while n > 0 : 
    cau_lenh , gia_tri = map(str, input().split())
    gia_tri = float(gia_tri) 

    if cau_lenh == "DEPOSIT" : 
        solve.deposit(gia_tri)
    elif cau_lenh == "WITHDRAW" : 
        solve.withdraw(gia_tri)
    n -= 1 

print(solve.__str__())