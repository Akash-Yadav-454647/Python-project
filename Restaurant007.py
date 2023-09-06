import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root", passwd="1 2 3 4 5 6" )
mycursor=mydb.cursor()

try:
    mycursor.execute("CREATE DATABASE HOTEL_MANAGEMENT")
    mydb = mysql.connector.connect(host="localhost",user="root", passwd="1 2 3 4 5 6", database ="HOTEL_MANAGEMENT" )
except:
      pass

try:
      mydb = mysql.connector.connect(host="localhost",user="root", passwd="1 2 3 4 5 6", database ="HOTEL_MANAGEMENT" )
      mycursor=mydb.cursor()
      mycursor.execute("CREATE TABLE FOOD_MENU (FOODCODE INT(5)PRIMARY KEY,ITEM CHAR(50),PRICE INT(6))")
      fd="insert into food_menu(foodcode,item,price) values(131,'Veg Burger',30),(132,'CheeseBurger',40),(133,'Paneer Burger',40),(134,'Double CheeseBurger',40),(135,'Paneer Cheese Burger',50),(136,'Garlic Burger',40),(137,'Spring Roll',40),(138,'Kathi Roll',40),(139,'Paneer Roll',40),(140,'Veg Roll',40),(141,'French Fries',30),(142,'Momos',40),(143,'Momos Fries',50),(144,'Chilly Paneer',70),(145,'Potato Chilly',40),(146,'Manchurian',40),(147,'Dry Manchurian',40),(148,'Paneer Manchurian',60),(149,'Soyabean Manchurian',40)"
      mycursor.execute(fd)
      mydb.commit()
      fd1="insert into food_menu(foodcode,item,price) values(113,'Cheese Paratha',40),(114,'Aalu Paratha',30),(115,'Pyaz Paratha',40),(116,'Aalu Pyaz Paratha',40),(117,'Paneer Paratha',50),(118,'Gobhi Paratha',40),(119,'Butter Paratha',40),(120,'Fried Rice',30),(121,'Manchurian Rice',40),(122,'Paneer Rice',40),(123,'Garlic Rice',40),(124,'Saijwan fried Rice',40),(125,'Veg Pasta',40),(126,'White Pasta',50),(127,'Cheese Pasta',50),(128,'Red Pasta',40),(129,'White Paneer Pasta',60),(130,'Red Paneer Pasta',60)"
      mycursor.execute(fd1)
      mydb.commit()
      fd3 = "insert into Food_Menu (Foodcode,Item,Price) values (101,'VegMaggie',(40)) , (102,'planeMaggie' ,30 ) , (103,'ButterMaggie',40),(104,'CheeseMaggie',40) ,(105,'BreadMaggie',40) , (106,'ManchurianMaggie',40),(107,'Butter Masala Maggie',40) , (108,'Soyabean Maggie',50),(109,'Chawmein Veg' , 30) , (110,'Paneer Chawmein',50) , (111,'Hakka Noodles',40),(112,'Soya Noodles',45)"
      mycursor.execute(fd3)
      mydb.commit()
except:
      pass

try:
    s="create table BILL_RECORDS(CUSTOMER_CODE INT(4) PRIMARY KEY ,ORDER_DATE varchar(12),NAME CHAR(20),CONTACT_NO VARCHAR(10) ,COST INT(6),MODE_OF_PAYMENT CHAR(10))"
    mycursor.execute(s)
    mydb.commit()
except:
      pass

mydb = mysql.connector.connect(host="localhost",user="root", passwd="1 2 3 4 5 6", database ="HOTEL_MANAGEMENT" )
mycursor=mydb.cursor()
try:
    mydb = mysql.connector.connect(host="localhost",user="root", passwd="1 2 3 4 5 6", database ="HOTEL_MANAGEMENT" )
    mycursor=mydb.cursor()
    s="Insert into BILL_RECORDS VALUES (1000,'05/10/20','Dipak','8109103198',400,'UPI')"
    mycursor.execute(s)
    mydb.commit()
except:
      pass


def placeorder():
      h=input("Enter your name:")
      print("Welcome ",h)
      mob=int(input("Enter mobile no:"))
      print("Format : DD/MM/YYYY")
      date=input("Enter Date:")
      s="SELECT * FROM FOOD_MENU"
      mycursor.execute(s)
      n=[]
      for k in mycursor:
            n.append(k)
      print("| FOODCODE                | ITEM                       | PRICE     |")
      print("------------------------------------------------------------------")
      for i in n:
          print("|",i[0]," "*(22-len(str(i[0]))),"|",i[1]," "*(30-len(i[1])),"|", i[2]," "*(6-len(str(i[2]))),"|")
      a=[]
      x=int(input("Enter Number Of Items :"))
      for i in range(0,x):
          y=int(input("Enter Food Code : "))
          z=int(input("Enter Quantity : "))
          s="select foodcode,item,price,%s from food_menu where foodcode = %s"%(z,y)
          mycursor.execute(s)
          data=mycursor.fetchall()
          for row  in data:
              a.append(row)
          
      D="select max(customer_code) from bill_records"
      mycursor.execute(D)
      data=mycursor.fetchone()
      for row in data:
            F=row
      S=F+1


      print("1. UPI")
      print("2. Wallets")
      print("3. Credit/Debit/ATM Card")
      print("4. Cash ")
      pay=int(input("Enter Mode Of Payment:"))
      xp=' '
      if pay==1:
            xp="UPI"
      elif pay==2:
            xp="Wallets"
      elif pay==3:
            xp="Card"
      else:
            xp="Cash"
      print("Payment Mode :",xp)
      print("Customer name :",h)
      print("Mobile Number :",mob)
      print()
      print("Do You Want To Change:")
      print("1.Yes")
      print('2.NO')
      Q=int(input("Enter Choice:"))
      if Q==1:
            h=input("Enter your name:")
            print("Welcome ",h)
            mob=int(input("Enter mobile no:"))
            print("Format : DD/MM/YYYY")
            date=input("Enter Date:")
            s="SELECT * FROM FOOD_MENU"
            mycursor.execute(s)
            n=[]
            for k in mycursor:
                n.append(k)
            print("| FOODCODE                | ITEM                       | PRICE    |")
            print("------------------------------------------------------------------")
            for i in n:
              print("|",i[0]," "*(22-len(str(i[0]))),"|",i[1]," "*(30-len(i[1])),"|", i[2]," "*(6-len(str(i[2]))),"|")
            a=[]
            x=int(input("Enter Number Of Items :"))
            for i in range(0,x):
                  y=int(input("Enter Food Code : "))
                  z=int(input("Enter Quantity : "))
                  s="select foodcode,item,price,%s from food_menu where foodcode = %s"%(z,y)
                  mycursor.execute(s)
                  data=mycursor.fetchall()
                  for row  in data:
                        a.append(row)
          
            D="select max(customer_code) from bill_records"
            mycursor.execute(D)
            data=mycursor.fetchone()
            for row in data:
                F=row
            S=F+1

            
            print("1. UPI")
            print("2. Wallets")
            print("3. Credit/Debit/ATM Card")
            print("4. Cash ")
            pay=int(input("Enter Mode Of Payment:"))
            xp=' '
            if pay==1:
                  xp="UPI"
            elif pay==2:
                  xp="Wallets"
            elif pay==3:
                  xp="Card"
            else:
                  xp="Cash"
            print("Payment Mode :",xp)
            print("Customer name :",h)
            print("Mobile Number :",mob)

      elif Q==2:
            print("Order Confirmed")
      else:
            print("Invalid Input")
      print()

      print("Your Order is :")
      print("_________________________________________________________")
      print("CUSTOMER CODE:",F+1)
      print("Foodcode|        Item               |Price|Quantity|Cost")
      print("---------------------------------------------------------")

      r=[]
      for i in range(0,x):
            y=0
            z=0
            b=list(a[i])
            c=b[2]*b[3]
            y=y+c
            m=list(a[i])
            m.append(y)
            print("|",m[0],""*(7-len(str(m[0]))),"|",m[1]," "*(25-len(m[1])),"|", m[2]," "*(2-len(str(m[2]))),"|",m[3]," "*(2-len(str(m[3]))),"|", m[4]," "*(3-len(str(m[4]))),"|")
            r.append(c)
      for i in r:
            z=z+i
      print("__________________________________________________________")
      print("Total Amount Of Order=",z)
      print()

      import random
      y=random.randint(5,20)
      print("Congratulations You Got A Discount Of ",y,"%")
      z=int(z-z*(y/100))
      print("Now You Have To Pay",z)
    
      l="insert into BILL_RECORDS values(%s,'%s','%s',%s,%s,'%s')"%(S,date,h,mob,z,xp)
      mycursor.execute(l)
      mydb.commit()
      print()
      return "Have A Nice Day"
      print(placeorder())

def manager():
      print("1.UPDATE")
      print("2.DELETE")
      print("3.Add")
      A=int(input("Enter Number Of What You Want:"))
      if A==1:
          print("You Want To Update")
          print("1.FoodCode")
          print("2.FoodName")
          print("3.Price")
          print()
          x=int(input("Enter Update Number:"))
          if x==1:
              
              k=int(input("Enter New Food Code:"))
              R=int(input("Enter Old Food Code:"))
              q="update food_menu set foodcode=%s where foodcode=%s "%(k,R)
              mycursor.execute(q)
              mydb.commit()
              return "Successfully Updated"
              print(manager())
          elif x==2:
              old=input("Enter Old Food Name:")
              new=input("Enter New Food Name:")
              que="update food_menu set item='%s' where item='%s' "%(new,old)
              mycursor.execute(que)
              mydb.commit()
              return "Successfully Updated"
              print(manager())
          elif x==3:
              op=int(input("Enter Food Code:"))
              np=int(input("Enter New Price:"))
              nop="update food_menu set price=%s where foodcode=%s "%(np,op)
              mycursor.execute(nop)
              mydb.commit()
              return "Successfully Updated"
              print(manager())
          else:
              return "Invalid Input"
              print(manager())
      elif A==2:
          W=int(input("Enter Food Code:"))
          q=[]
          b=[]
          q.append(W)
          A="select foodcode from food_menu"
          mycursor.execute(A)
          data=mycursor.fetchall()
          for row in data:
              b.append(list(row))
          if q in b:
              E="delete from food_menu where foodcode=%s "%W
              mycursor.execute(E)
              mydb.commit()
              return "Successfully Deleted"
              print(manager())              
          else:
              return "Invalid input"
              print(manager())
      elif  A==3:
              
          q=[]
          a="select max(foodcode) from food_menu"
          mycursor.execute(a)
          data=mycursor.fetchone()
          for row in data:
              q.append(row)
              G=q[0]+1
              b=str(input("Enter Food Name"))
              c=int(input("Enter Food Price"))
              D="insert into food_menu values(%s,'%s',%s)"%(G,b,c)
              mycursor.execute(D)
              return "Successfully Added"
              print(manager())
 
      else:
          return "Invalid Input"
          print(manager())



def records():
      print("You Want To Check:")
      print("1.Total Sale")
      print("2.Sale By Date")
      print("3.Customer Detail")
      print()
      N=int(input("Enter Number According To What You Want To Check : "))
      if N==1:
            S="select sum(cost) from bill_records"
            mydb = mysql.connector.connect(host="localhost",user="root", passwd="1 2 3 4 5 6", database ="HOTEL_MANAGEMENT" )
            mycursor=mydb.cursor()
            mycursor.execute(S)
            data=mycursor.fetchone()
            for row  in data:
                  print("Total Sale")
            return row
            print(records())
      elif N==2:
            Q=[]
            q=int(input("Enter No Of Days"))
            for i in range(0,q):
                  e=str(input("Enter Date: "))
                  mydb = mysql.connector.connect(host="localhost",user="root", passwd="1 2 3 4 5 6", database ="HOTEL_MANAGEMENT" )
                  mycursor=mydb.cursor()
                  A="select sum(cost) from bill_records where order_date='%s'"%e
                  mycursor.execute(A)
                  totcos=mycursor.fetchone()
                  for row in totcos:
                      print("Date"+" "*(len(e)-3)+"| Totalcost")
                      print(e,"|",row)
            return "DONE!!!"
            print(records())
      elif N==3:
            P=[]
            u=int(input("Enter Customer Code:"))
            mydb = mysql.connector.connect(host="localhost",user="root", passwd="1 2 3 4 5 6", database ="HOTEL_MANAGEMENT" )
            mycursor=mydb.cursor()
            X="select * from bill_records where customer_code=%s"%u
            mycursor.execute(X)
            data=mycursor.fetchone()
            for row in data:
                  P.append(row)
            print()
            print("Customer Code:",P[0])
            print()
            print("Order Date:",P[1])
            print()
            print("Customer Name:",P[2])
            print()
            print("Contact Number:",P[3])
            print()
            print("Paid:",P[4])
            print()
            print("Mode Of Payment:",P[5])
            return "DONE!!!"
            print(records())
            
      else:
            return "Invalid Input"
            print(records())

                  
def billrecords():
      Q="Select count(customer_code) from bill_records"
      mycursor.execute(Q)
      data=mycursor.fetchone()
      for row in data:
            print(row)
      P="select * from bill_records"
      mycursor.execute(P)
      for i in range(0,row):
            da=mycursor.fetchone()
            print("--------------------------------------------------")
            print("Record Number : ",i+1)
            print("Customer Code:",da[0])
            print()
            print("Order Date:",da[1])
            print()
            print("Customer Name:",da[2])
            print()
            print("Contact Number:",da[3])
            print()
            print("Paid:",da[4])
            print()
            print("Mode Of Payment:",da[5])
            print("--------------------------------------------------")
            print()
            print()
      print("Enter 1 For  Yes And  2 For No")
      R=int(input("Do You Want To Change In Records : "))
      if R==1:
             print("1.UPDATE")
             print("2.DELETE")
             A=int(input("Enter Choice:"))
             if A==1:
                   print("You Want To Update:")
                   print("1.Name")
                   print("2.Contact Number")
                   y=int(input("Enter choice :"))
                   if y==1:
                         g=str(input("Enter Name"))
                         c=int(input("Enter Customer Code"))
                         E="update bill_records set  name='%s' where customer_code=%s"%(g,c)
                         mycursor.execute(E)
                         mydb.commit()
                         return "SUCCESSFULLY UPDATED"
                         print(billrecords())
                   elif y==2:
                         D=int(input("Enter Customer Code:"))
                         x=int(input("Enter Contact Number :"))
                         V="update bill_records set  contact_no=%s where customer_code=%s"%(x,D)
                         mycursor.execute(V)
                         mydb.commit()
                         return "SUCCESSFULLY UPDATED"
                         print(billrecords())
                   else:
                         print("Invalid Input")
             elif A==2:
                    d=int(input("Enter Customer Code:"))
                    S="delete from bill_records where customer_code=%s"%d
                    mycursor.execute(S)
                    mydb.commit()
                    return "Successfully Deleted"
                    print(billrecords())
      elif R==2:
            return "Have a Great time"
            print(billrecords())
      else:
            return "Invalid Input"
            print(billrecords())
k="Y"
while k=="Y" or k=="y":
    print("Hello User Welcome to Restaurant")

    print("Enter your choice ")
    print("1. Placeorder")
    print("2. Manager")
    print("3. Records")
    print("4. Billrecords")
    c=int(input("Enter no"))
    if c==1:
        print(placeorder())
    elif c==2:
        print(manager())
    elif c==3:
        print(records())
    elif c==4:
        print(billrecords())
    else:
        print("Invalid choice")
    k=input("To continue 'Y' and for not 'N' ")







          


