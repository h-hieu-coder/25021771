#Bai 8 Tinh tien dien
name = input("Ten chu ho : ")
before = int(input("Chi so thang truoc :"))
after = int(input("Chi so thang nay :"))
num = after - before
money = 0
#bac 1
if(num<=50):
    money = num*1984
#bac 2
elif(50<num and num<=100):
    money = 50*1984 + (num-50)*2050
#bac 3
elif(100<num and num<=200):
    money = 50*1984 + 50*2050 +(num -100)*2380
#bac 4
elif(200<num and num<=300):
    money = 50*1984 + 50*2050 +100*2380 +(num-200)*2998
#bac 5
elif(300<num and num<=400):
    money = 50*1984 + 50*2050 +100*2380 +100*2998 +(num-300)*3350
#bac 6
else :
    money = 50*1984 + 50*2050 +100*2380 +100*2998 +100*3350 +(num-400)*3460
print(round(money*1.08))