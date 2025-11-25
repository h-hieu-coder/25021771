num1 = 1
num2 = 1
A = int(input())
while num2 <= A : 
    num1, num2 = num2, (num1 + num2)
print(num1)