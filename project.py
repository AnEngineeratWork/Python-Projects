import mysql.connector as sqltor
connector = sqltor.connect(host='localhost',user='root',passwd='Njk17zads',database='testing')
cursor =connector.cursor()
query=''

print("\n\n  Airline Ticket Booking System\n")
restart = 'y'

while restart != ('N', 'NO', 'n', 'no'):
    print("1. Check booking status")
    print("2. Ticket Reservation")
    print("3.Book Meals")
    print("4. Exit")
    option = int(input("\n Enter your option:"))


    if option == 1:
        uid = input("Enter your user id:")
        query = "select name, age, gender from info where user_id='{}'".format(uid)
        cursor.execute(query)
        f=cursor.fetchone()
        while f is not None:
            print(f)
            f=cursor.fetchone()

    elif option == 2:
        user__id = input("Enter your user id:")
        pass__ =input("Enter your password:")
        query="insert into users(user_id, passwords) values('{}','{}')".format(user__id, pass__)
        print("Login successful. Proceed with your booking.")
        people = int(input("\n Enter no. of Ticket(s) you want:"))
        for p in range(1, people + 1):
            name_ = input("\n Name of passenger number" + str(p) + ":")
            age_ = int(input("\n Age of the passenger:"))
            sex_ = input("\n Gender of the passenger:")
            query = "insert into info(user_id, name, age, Gender) values('{}','{}',{},'{}')".format(user__id, name_, age_, sex_)
            cursor.execute(query)
            connector.commit()

        choice=input("Do you want to continue?:")
        if choice in ('YES','yes', 'Yes','y','Y'):
            restart='y'

    elif option == 3:
        uid=input("Enter your User ID:")
        print("\n Available beverages are:")
        query = "select id,n_o_m,cost from meals where type='{}'".format('Beverage')
        cursor.execute(query)
        f = cursor.fetchone()
        while f is not None:
            print(f)
            f = cursor.fetchone()
        print("\n Available Full Course Meals are:")
        query = "select id,n_o_m,cost from meals where type='{}'".format('Full course')
        cursor.execute(query)
        f = cursor.fetchone()
        while f is not None:
            print(f)
            f = cursor.fetchone()
        print("\n Available Starters are:")
        query = "select id,n_o_m,cost from meals where type='{}'".format('Starters')
        cursor.execute(query)
        f = cursor.fetchone()
        while f is not None:
            print(f)
            f = cursor.fetchone()
        print("\n Available deserts are:")
        query = "select id,n_o_m,cost from meals where type='{}'".format('Deserts')
        cursor.execute(query)
        f = cursor.fetchone()
        while f is not None:
            print(f)
            f = cursor.fetchone()
        v = True
        while v==True:
            ch = int(input("Enter id of food you want to order: "))
            query = "select n_o_m from meals where id={}".format(ch)
            cursor.execute(query)
            nm = cursor.fetchall()
            nm = str(nm[0])
            nm = eval(nm)
            nm = nm[0]
            query = "select cost from meals where id={}".format(ch)
            cursor.execute(query)
            cs = cursor.fetchall()
            cs = str(cs[0])
            cs = eval(cs)
            cs = cs[0]
            query = "insert into orders (user_id,id,n_o_m,cost) values ('{}',{},'{}',{})".format(uid,ch,nm,cs)
            cursor.execute(query)
            connector.commit()
            ct = input("\n Want to order more?(y/n):")
            if ct in ('y','Y'):
                v = True
            else:
                v = False
        print("Booked meals are:")
        query = "select n_o_m,cost from orders where user_id='{}'".format(uid)
        cursor.execute(query)
        f = cursor.fetchone()
        while f is not None:
            print(f)
            f = cursor.fetchone()

    elif option==4:
        print("Thank you for using our services.")
        break

connector.close()
