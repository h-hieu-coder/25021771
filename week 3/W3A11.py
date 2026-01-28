a , b, c = map(int , input().split())
if((a+b>c) and (a+c>b) and (b+c>a)):
  if(a==b and b==c) :
    print("Tam giac deu")
  elif(a==b or a==c or b==c) :
    print("Tam giac can")
  else : print("Tam giac thuong")
else : print("Khong phai tam giac")