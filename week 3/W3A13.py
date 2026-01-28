so_dien = int(input())
money = 0
if (so_dien>0 and so_dien<=50) :
    money = so_dien*1500
elif (so_dien>50 and so_dien<=100):
    money = 50*1500 + (so_dien-50)*2000
else :
    money = 50*1500 + 50*2000 + (so_dien-100)*3000
print(money)