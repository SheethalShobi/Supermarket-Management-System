import mysql.connector as c
from datetime import date
con=c.connect(host="localhost",user="root",passwd="bvm",database="project")

list2=[]
sum=0
num=int(input("enter number of items purchased: "))
for i in range(0,num):
      items=int(input("enter name of item"))
      qty=int(input("enter quantity"))
      cur.execute("select * from food where fname='{}'".format(items))
      x=cur.fetchall()
      if len(x)==0:
            print ("no such food is available")
            break
      for i in x:
            price=i[3]
      amount=qty*price
      list1=[food,qty,price,amount]
      list2=list2+list1
if len(x)==0:
      print("cannot process bill")
else:
      u=t[0]
      name=u[0]
      print("ready to process bill")
print()
if len(t)==0:
      print("cannot process bill")
else:
      print(" "*14,"MARGIN FREE SUPERMARKET"," "*14)
      print(" "*14,"--------------------------------------------"," "*14)
      print(" "*20,"BILL"," "*20)
      print(" "*20,"------"," "*20)
      print("name of the customer"," "*15,":",name)
      today=data.today()
      print("date"," "*31,":",today)
      print()
      print("item name"+" "*7,"quantity","price","amount",sep=" ")
      print("-"*44)
      for j in range(1,num+1):
            print(list2[0]+" "*(20-len(list2[0])),str(list2[1])+" "*(5-len(str(list2[1]))),str(list2[2])+" "*(5-len(str(list2[2]))),list2[3],sep=" ")
            sum=sum+list2[3]
            list2.reverse()
            for k in range(0,4):
                  list2.pop()
            list2.reverse()
      print()
      print(" "*27,"sub total:",sum)
      print(" "*32,"CGST: 9%")
      print(" "*32,"SGST: 9%")
      total=sum*(118/100)
      print(" "*25,"Grand total: ",round(total,2))
      print("\nThank You for your visit.Have a nice day!")
      
