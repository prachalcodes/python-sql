import mysql.connector as conn
import pandas as pd
import matplotlib.pyplot as plt


db=conn.connect(host="localhost",
                user="root",
                password="root",
                database="carstore")
if db.is_connected():
    print("Mysql Connection Successful")

print('''
----------------------------------------
        CAR SPARE PART STORE
----------------------------------------
''')

while True:
    print('''
1) Admin
2) User''')    

    ch=int(input("Please select between 1-2: "))
    if ch==1:
        print('''
1) Display Records
2) Insert Records
3) Modify Records ''')
        ch=int(input("Please select between 1-3: "))
        if ch==1:
            print('''
Choose the table you want to display
1) Vehicle
2) Supplier
3) Parts
4) Customers
5) Purchase
6) Returns ''')
            ch=int(input("Please select between 1-6: "))
            print("")
            if ch==1:
                cond=input("Conditions (press enter if none): ")
                print("")
                cur=db.cursor()
                query="select * from vehicle "+cond+";" 
                cur.execute(query)
                record=cur.fetchall()
                print("Vehicle_id Company  Model")
                for i in record:
                    print(i)
            elif ch==2:
                cond=input("Conditions (press enter if none): ")
                print("")
                cur=db.cursor()
                query="select * from supplier "+cond+";" 
                cur.execute(query)
                record=cur.fetchall()
                print("Supplier Name\t\t\t  Email")
                for i in record:
                    print(i)
            elif ch==3:
                cond=input("Conditions (press enter if none): ")
                print("")
                cur=db.cursor()
                query="select * from parts "+cond+";" 
                cur.execute(query)
                record=cur.fetchall()
                print("Part_id Name Details Price Qty Vehicle_id Supplier_id")
                for i in record:
                    print(i)
            elif ch==4:
                cond=input("Conditions (press enter if none): ")
                print("")
                cur=db.cursor()
                query="select * from customer "+cond+";" 
                cur.execute(query)
                record=cur.fetchall()
                print("Cust_id Name Email Address Part_id Qty")
                for i in record:
                    print(i)
            elif ch==5:
                cond=input("Conditions (press enter if none): ")
                print("")
                cur=db.cursor()
                query="select * from purchase "+cond+";" 
                cur.execute(query)
                record=cur.fetchall()
                print("Sr.No. Date\t\t\t Part_id Qty")
                for i in record:
                    print(i)
            elif ch==6:
                cond=input("Conditions (press enter if none): ")
                print("")
                cur=db.cursor()
                query="select * from returns "+cond+";" 
                cur.execute(query)
                record=cur.fetchall()
                print("Sr.No. Date Part_id Cust_id Qty")
                for i in record:
                    print(i)
            else:
                print("Invalid Input")
        elif ch==2:
            print('''
Choose the table you want to insert record into
1) Vehicle
2) Supplier
3) Parts
4) Purchase ''')
            ch=int(input("Please select between 1-4: "))
            print("")
            if ch==1:
                cur=db.cursor()
                cur.execute("select * from vehicle;")
                record=cur.fetchall()
                print("Vehicle_Id Company Model")
                for i in record:
                    print(i)
                print("")
                
                veh_id = input("Enter Vehicle Id: ")
                veh_comp = input("Enter Vehicle Company: ")
                veh_model = input("Enter Vehicle Model: ")
                print("")
                
                query="insert into vehicle values ('{}','{}','{}')".format(veh_id,veh_comp,veh_model)
                cur.execute(query)
                db.commit()
                print("Data Inserted Successfully")
                print("")
                
                cur.execute("select * from vehicle;")
                record=cur.fetchall()
                print("Vehicle_Id Company Model")
                for i in record:
                    print(i)
                print("")
            elif ch==2:
                cur=db.cursor()
                cur.execute("select * from supplier;")
                record=cur.fetchall()
                print("Supplier Name\t\t\t  Email")
                for i in record:
                    print(i)
                print("")
                
                sp_id = input("Enter Supplier Id: ")
                sp_name = input("Enter Supplier Name: ")
                sp_email = input("Enter Supplier Email: ")
                print("")
                
                query="insert into supplier values ('{}','{}','{}')".format(sp_id,sp_name,sp_email)
                cur.execute(query)
                db.commit()
                print("Data Inserted Successfully")
                print("")
                
                cur.execute("select * from supplier;")
                record=cur.fetchall()
                print("Supplier Name\t\t\t  Email")
                for i in record:
                    print(i)
                print("")
            elif ch==3:
                cur=db.cursor()
                cur.execute("select * from vehicle;")
                record=cur.fetchall()
                print("Vehicle_Id Company Model")
                for i in record:
                    print(i)
                print("")

                cur.execute("select * from supplier;")
                record=cur.fetchall()
                print("Supplier Name\t\t\t  Email")
                for i in record:
                    print(i)
                print("")
                
                cur.execute("select * from parts;")
                record=cur.fetchall()
                print("Part_id Name Details Price Qty Vehicle_id Supplier_id")
                for i in record:
                    print(i)
                print("")
                
                cp_id = input("Enter Car Part Id: ")
                cp_name = input("Enter Car Name: ")
                spec = input("Car Details: ")
                price = int(input("Enter price: "))
                qty = int(input("Quantity: "))
                veh_id = input("Enter Vehicle Id: ")
                sp_id = input("Enter Supplier Id: ")
                print("")
                
                query="insert into parts values ('{}','{}','{}',{},{},'{}','{}')".format(cp_id,cp_name,spec,price,qty,veh_id,sp_id)
                cur.execute(query)
                db.commit()
                print("Data Inserted Successfully")
                print("")

                cur.execute("select * from parts;")
                record=cur.fetchall()
                print("Part_id Name Details Price Qty Vehicle_id Supplier_id")
                for i in record:
                    print(i)
                print("")
            elif ch==4:
                cur=db.cursor()
                cur.execute("select * from parts;")
                record=cur.fetchall()
                print("Part_id Name Details Price Qty Vehicle_id Supplier_id")
                for i in record:
                    print(i)
                print("")

                cur.execute("select * from purchase;")
                record=cur.fetchall()
                print("Sr.No. Date Part_id Qty")
                for i in record:
                    print(i)
                print("")

                pur_no = input("Enter Purchase No.: ")
                pur_date = input("Enter Date: ")
                cp_id = input("Enter Car Part Id: ")
                qty = input("Enter quantity: ")
                print("")
                
                query = "insert into purchase values('{}','{}','{}',{})".format(pur_no,pur_date,cp_id,qty)
                cur.execute(query)
                db.commit()
                print("Data Inserted Successfully")
                print("")

                cur.execute("select * from purchase;")
                record=cur.fetchall()
                print("Sr.No. Date Part_id Qty")
                for i in record:
                    print(i)
                print("")
            else:
                print("Invalid Input")
        elif ch==3:
            print('''
Choose the table you want to update
1) Vehicle
2) Supplier
3) Parts
4) Purchase ''')
            ch=int(input("Please select between 1-4: "))
            if ch==1:
                ch=int(input('''
Choose the field you want to update
1) Vehicle Company
2) Vehicle Model
Please select between 1-2: '''))
                if ch==1:
                    cur=db.cursor()
                    cur.execute("select * from vehicle;")
                    record=cur.fetchall()
                    print("Vehicle_Id Company Model")
                    for i in record:
                        print(i)
                    print("")

                    veh_id=input("Enter Vehicle Id: ")
                    veh_comp=input("Enter Vehicle Company: ")
                    print("")
                    
                    query="update vehicle set veh_comp='{}' where veh_id='{}'".format(veh_comp,veh_id)
                    cur.execute(query)
                    db.commit()
                    print("Data Updated Successfully")
                    print("")
                    
                    cur.execute("select * from vehicle;")
                    record=cur.fetchall()
                    print("Vehicle_Id Company Model")
                    for i in record:
                        print(i)
                    print("")
                elif ch==2:
                    cur=db.cursor()
                    cur.execute("select * from vehicle;")
                    record=cur.fetchall()
                    print("Vehicle_Id Company Model")
                    for i in record:
                        print(i)
                    print("")

                    veh_id=input("Enter Vehicle Id: ")
                    veh_model=input("Enter Vehicle Model: ")
                    print("")
                    
                    query="update vehicle set veh_model='{}' where veh_id='{}'".format(veh_model,veh_id)
                    cur.execute(query)
                    db.commit()
                    print("Data Updated Successfully")
                    print("")
                    
                    cur.execute("select * from vehicle;")
                    record=cur.fetchall()
                    print("Vehicle_Id Company Model")
                    for i in record:
                        print(i)
                    print("")
                else:
                    print("Invalid Input")
            elif ch==2:
                ch=int(input('''Choose the field you want to update
1) Supplier Name
2) supplier Email Id
Please select between 1-2: '''))
                if ch==1:
                    cur=db.cursor()
                    cur.execute("select * from supplier;")
                    record=cur.fetchall()
                    print("Supplier Name\t\t\t  Email")
                    for i in record:
                        print(i)
                    print("")
                
                    sp_id = input("Enter Supplier Id: ")
                    sp_name = input("Enter Supplier Name: ")
                    print("")
                    
                    query="update supplier set sp_name='{}' where sp_id='{}'".format(sp_name,sp_id)
                    cur.execute(query)
                    db.commit()
                    print("Data Updated Successfully")
                    print("")
                    
                    cur.execute("select * from supplier;")
                    record=cur.fetchall()
                    print("Supplier Name\t\t\t  Email")
                    for i in record:
                        print(i)
                    print("")
                elif ch==2:
                    cur=db.cursor()
                    cur.execute("select * from supplier;")
                    record=cur.fetchall()
                    print("Supplier Name\t\t\t  Email")
                    for i in record:
                        print(i)
                    print("")
                
                    sp_id = input("Enter Supplier Id: ")
                    sp_email = input("Enter Supplier Email: ")
                    print("")
                    
                    query="update supplier set sp_email='{}' where sp_id='{}'".format(sp_email,sp_id)
                    cur.execute(query)
                    db.commit()
                    print("Data Updated Successfully")
                    print("")
                    
                    cur.execute("select * from supplier;")
                    record=cur.fetchall()
                    print("Supplier Name\t\t\t  Email")
                    for i in record:
                        print(i)
                    print("")
            elif ch==3:
                ch=int(input('''Choose the field you want to update
1) Part name
2) Specifications
3) Price
4) Quantity
5) Vehicle Id
6) Supplier Id
Please select between 1-6: '''))
                if ch==1:
                    cur=db.cursor()
                    cur.execute("select * from parts;")
                    record=cur.fetchall()
                    print("Part_id Name Details Price Qty Vehicle_id Supplier_id")
                    for i in record:
                        print(i)
                    print("")
                
                    cp_id = input("Enter Car Part Id: ")
                    cp_name = input("Enter Car Name: ")
                    print("")
                    
                    query="update parts set cp_name='{}' where cp_id='{}'".format(cp_name,cp_id)
                    cur.execute(query)
                    db.commit()
                    print("Data Updated Successfully")
                    print("")

                    cur.execute("select * from parts;")
                    record=cur.fetchall()
                    print("Part_id Name Details Price Qty Vehicle_id Supplier_id")
                    for i in record:
                        print(i)
                    print("")
                elif ch==2:
                    cur=db.cursor()
                    cur.execute("select * from parts;")
                    record=cur.fetchall()
                    print("Part_id Name Details Price Qty Vehicle_id Supplier_id")
                    for i in record:
                        print(i)
                    print("")
                
                    cp_id = input("Enter Car Part Id: ")
                    spec = input("Enter Specification: ")
                    print("")
                    
                    query="update parts set spec='{}' where cp_id='{}'".format(spec,cp_id)
                    cur.execute(query)
                    db.commit()
                    print("Data Updated Successfully")
                    print("")

                    cur.execute("select * from parts;")
                    record=cur.fetchall()
                    print("Part_id Name Details Price Qty Vehicle_id Supplier_id")
                    for i in record:
                        print(i)
                    print("")
                elif ch==3:
                    cur=db.cursor()
                    cur.execute("select * from parts;")
                    record=cur.fetchall()
                    print("Part_id Name Details Price Qty Vehicle_id Supplier_id")
                    for i in record:
                        print(i)
                    print("")
                
                    cp_id = input("Enter Car Part Id: ")
                    price = int(input("Enter Price: "))
                    print("")
                    
                    query="update parts set price={} where cp_id='{}'".format(price,cp_id)
                    cur.execute(query)
                    db.commit()
                    print("Data Updated Successfully")
                    print("")

                    cur.execute("select * from parts;")
                    record=cur.fetchall()
                    print("Part_id Name Details Price Qty Vehicle_id Supplier_id")
                    for i in record:
                        print(i)
                    print("")
                elif ch==4:
                    cur=db.cursor()
                    cur.execute("select * from parts;")
                    record=cur.fetchall()
                    print("Part_id Name Details Price Qty Vehicle_id Supplier_id")
                    for i in record:
                        print(i)
                    print("")
                
                    cp_id = input("Enter Car Part Id: ")
                    qty = int(input("Enter Quantity: "))
                    print("")
                    
                    query="update parts set qty={} where cp_id='{}'".format(qty,cp_id)
                    cur.execute(query)
                    db.commit()
                    print("Data Updated Successfully")
                    print("")

                    cur.execute("select * from parts;")
                    record=cur.fetchall()
                    print("Part_id Name Details Price Qty Vehicle_id Supplier_id")
                    for i in record:
                        print(i)
                    print("")
                elif ch==5:
                    cur=db.cursor()
                    cur.execute("select * from parts;")
                    record=cur.fetchall()
                    print("Part_id Name Details Price Qty Vehicle_id Supplier_id")
                    for i in record:
                        print(i)
                    print("")
                
                    cp_id = input("Enter Car Part Id: ")
                    veh_id = input("Enter Vehicle Id: ")
                    print("")
                    
                    query="update parts set veh_id='{}' where cp_id='{}'".format(veh_id,cp_id)
                    cur.execute(query)
                    db.commit()
                    print("Data Updated Successfully")
                    print("")

                    cur.execute("select * from parts;")
                    record=cur.fetchall()
                    print("Part_id Name Details Price Qty Vehicle_id Supplier_id")
                    for i in record:
                        print(i)
                    print("")
                elif ch==6:
                    cur=db.cursor()
                    cur.execute("select * from parts;")
                    record=cur.fetchall()
                    print("Part_id Name Details Price Qty Vehicle_id Supplier_id")
                    for i in record:
                        print(i)
                    print("")
                
                    cp_id = input("Enter Car Part Id: ")
                    sp_id = input("Enter Supplier Id: ")
                    print("")
                    
                    query="update parts set sp_id='{}' where cp_id='{}'".format(sp_id,cp_id)
                    cur.execute(query)
                    db.commit()
                    print("Data Updated Successfully")
                    print("")

                    cur.execute("select * from parts;")
                    record=cur.fetchall()
                    print("Part_id Name Details Price Qty Vehicle_id Supplier_id")
                    for i in record:
                        print(i)
                    print("")
                else:
                    print("Invalid Input")
            elif ch==4:
                ch=int(input('''Choose the field you want to update
1) Purchase Date
2) Car Part Id
3) Quantity
Please select between 1-3: '''))
                if ch==1:
                    cur=db.cursor()
                    cur.execute("select * from purchase;")
                    record=cur.fetchall()
                    print("Sr.No. Date Part_id Qty")
                    for i in record:
                        print(i)
                    print("")

                    pur_no = input("Enter Purchase No.: ")
                    pur_date = input("Enter Date: ")
                    print("")
                    
                    query = "update purchase set pur_date='{}' where pur_no='{}'".format(pur_date,pur_no)
                    cur.execute(query)
                    db.commit()
                    print("Data Updated Successfully")
                    print("")

                    cur.execute("select * from purchase;")
                    record=cur.fetchall()
                    print("Sr.No. Date Part_id Qty")
                    for i in record:
                        print(i)
                    print("")
                elif ch==2:
                    cur=db.cursor()
                    cur.execute("select * from purchase;")
                    record=cur.fetchall()
                    print("Sr.No. Date Part_id Qty")
                    for i in record:
                        print(i)
                    print("")

                    pur_no = input("Enter Purchase No.: ")
                    cp_id = input("Enter Car Part Id: ")
                    print("")
                    
                    query = "update purchase set cp_id='{}' where pur_no='{}'".format(cp_id,pur_no)
                    cur.execute(query)
                    db.commit()
                    print("Data Updated Successfully")
                    print("")

                    cur.execute("select * from purchase;")
                    record=cur.fetchall()
                    print("Sr.No. Date Part_id Qty")
                    for i in record:
                        print(i)
                    print("")
                elif ch==3:
                    cur=db.cursor()
                    cur.execute("select * from purchase;")
                    record=cur.fetchall()
                    print("Sr.No. Date Part_id Qty")
                    for i in record:
                        print(i)
                    print("")

                    pur_no = input("Enter Purchase No.: ")
                    qty = int(input("Enter Quantity: "))
                    print("")
                    
                    query = "update purchase set qty={} where pur_no='{}'".format(qty,pur_no)
                    cur.execute(query)
                    db.commit()
                    print("Data Updated Successfully")
                    print("")

                    cur.execute("select * from purchase;")
                    record=cur.fetchall()
                    print("Sr.No. Date Part_id Qty")
                    for i in record:
                        print(i)
                    print("")
                else:
                    print("Invalid Input")
            else:
                print("Invalid Input")
        else:
            print("Invalid Input")
    elif ch==2:
        print('''
1) Buy Car Parts
2) Return Car Parts ''')
        ch=int(input("Please select between 1-2: "))
        if ch==1:
            cur=db.cursor()
            cur.execute("select cp_id,cp_name,spec,price from parts")
            record=cur.fetchall()
            print("Part_id Name Details Price")
            for i in record:
                print(i)
            print("")

            cust_id="C12"
            cust_name=input("Enter your name: ")
            cust_email=input("Enter your email: ")
            cust_add=input("Enter your address: ")
            cp_id=input("Enter Car Part Id: ")
            qty=int(input("Enter the quantity: "))
            cust_date=input("Enter Date (YYYY-MM-DD): ")
            print("")
            
            query="insert into customer values ('{}','{}','{}','{}','{}',{},'{}')".format(cust_id,cust_name,cust_email,cust_add,cp_id,qty,cust_date)
            cur.execute(query)
            db.commit()
            print("Purchase Successful")
            print("")
        elif ch==2:
            cur=db.cursor()
            cur.execute("select * from customer;")
            record=cur.fetchall()
            print("Bill_No. Name\t\t Email_Id\t Address \t\tPart_Id Quantity Date")
            for i in record:
                print(i)
            print("")
            
            ret_id="R06"
            ret_date=input("Enter Date of Return (YYYY-MM-DD): ")
            cp_id=input("Enter Car Part you want to Return: ")
            cust_id=input("Enter your bill no.: ")
            qty=int(input("Enter quantity you want to return: "))
            print("")
            
            query="insert into returns values ('{}','{}','{}','{}',{})".format(ret_id,ret_date,cp_id,cust_id,qty)
            cur.execute(query)
            db.commit()
            print("Return Successful")
            print("")
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
    print("")
    print("-------------------------------------------------------------------")
