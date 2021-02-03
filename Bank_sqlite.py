import sqlite3
from Bank import Info

connect = sqlite3.connect("BankDB.db")

c = connect.cursor()
#while(True):
#c.execute("CREATE TABLE customer_info(name text,account_number text,account_password text,address text,reg_num text,left )")
#    break
def withdraw(data,ini_withdraw2):
    if int(data.get_left()) <int(ini_withdraw2):
        print("The amount you want to withdraw is larger than the amount in your account")
        return None
    elif int(data.get_left()) >= int(ini_withdraw2):
        data.set_left((int(data.get_left()) - int(ini_withdraw2)))
        with connect:
            c.execute("""UPDATE customer_info SET left=:left
            WHERE name=:name AND account_number=:account_number AND account_password=:account_password AND address=:address AND reg_num=:reg_num""",
                      {'name':data.get_name, 'account_number':data.get_acc_num(), "account_password":data.get_add_pass(), 'address':data.get_addr(), "reg_num":data.get_reg_num(), 'left':data.get_left()})
        return data.get_left()
def deposit(data,ini_left123):
    if data.get_left()  is not None:
        data.set_left((int(data.get_left()) + int(ini_left123)))
        with connect:
            c.execute("""UPDATE customer_info SET left=:left
            WHERE name=:name AND account_number=:account_number AND account_password=:account_password AND address=:address AND reg_num=:reg_num""",
                      {'name':data.get_name, 'account_number':data.get_acc_num(), "account_password":data.get_add_pass(), 'address':data.get_addr(), "reg_num":data.get_reg_num(), 'left':data.get_left()})
    elif data.get_left() is None:
        data.set_left(int(ini_left123))
        with connect:
            c.execute("""UPDATE customer_info SET left=:left
            WHERE name=:name AND account_number=:account_number AND account_password=:account_password AND address=:address AND reg_num=:reg_num""", {'name':data.get_name, 'account_number':data.get_acc_num(), "account_password":data.get_add_pass(), 'address':data.get_addr(), "reg_num":data.get_reg_num(), 'left':data.get_left()})

def search_with_num(num):
    c.execute("SELECT * FROM customer_info WHERE account_number=:account_number",{'account_number':num})
    return c.fetchone()

def search_with_pass(pass_):
    c.execute("SELECT * FROM customer_info WHERE account_password=:account_password",{'account_password':pass_})
    return c.fetchone()

def search_data(num,password):
    c.execute("SELECT * FROM customer_info WHERE account_number=:account_number AND account_password=:account_password", {'account_number': num,'account_password':password})
    return c.fetchone()

def Insert_data(data):
    with connect:
        c.execute( "INSERT INTO customer_info VALUES(:name,:account_number,:account_password,:address,:reg_num,:left)", {'name':data.get_name, "account_number":data.get_acc_num(), "account_password":data.get_add_pass(), "address":data.get_addr(), "reg_num":data.get_reg_num(), "left":data.get_left()})

def Welcome():
    print("Welcome to the Grace Bank")
    print("Press 1 to create an Account")
    print("Press 2 to search for your Personal Information")
    print("Press 3 to deposit")
    print("Press 4 to withdraw")
    print("Press 5 to Quit")
global thing
while(True):
    try:
        thing=int(input("Welcome to the Grace Bank\nPress 1 to create an Account\nPress 2 to search for your Personal Information\nPress 3 to deposit\nPress 4 to withdraw\nPress 5 to Quit\nEnter : "))
    except ValueError:
        print("Please check if you had inputted the right option")
    if thing is 1:
        ini_name = input("Enter your name")

        while True:
            ini_acc_num = input("Enter the account number you'll use")
            if123 = search_with_num(ini_acc_num)
            if if123 is None:
                break
            elif if123 is not None:
                print("your account number is already in use. Please enter different account number")
        while True:
            ini_acc_pass = input("Enter the password you'll use")
            conf_pass = input("Confirm your password")
            if ini_acc_pass==conf_pass:
                break
        ini_addr = input("Enter your home address")
        ini_regnum = input("Enter your identity number")
        insert = Info(ini_name,ini_acc_num,ini_acc_pass,ini_addr,ini_regnum,1)
        Insert_data(insert)
        print("name : ",ini_name)
        print("account number : ",ini_acc_num)
        print("account password : ",ini_acc_pass)
        print("address : ",ini_addr)
        print("identity number : ",ini_regnum)
        print("successfully made")

    elif thing is 2:
        while True:
            account= input("Enter your account number")
            a = search_with_num(account)
            if a is None:
                print("your account number is not in our database. Please check if your account number is correct")
            elif a is not None:
                break
        while True:
            password = input("Enter your password")
            a1 = search_with_pass(password)
            if a1 is None:
                print("your password doesn't match with your account number")
            elif a is not None:
                break
        search = search_data(account,password)
        print(search)

    elif thing is 3:
        while True:
            account_num = input("input your account number")
            q = search_with_num(account_num)
            if q is None:
                print("Your account number is not in our database")
            elif q is not None:
                break
        while True:
            account_pass = input("Enter your account password")
            q1 = search_with_pass(account_pass)
            if q1 is None:
                print("Your password doesn't match your account number")#함수
            elif q1 is not None:
                break
        put = input("Input the amount you will deposit")
        ini = search_data(account_num,account_pass)
        #print(ini)
        na = ini[0]
        nu = ini[1]
        pa = ini[2]
        ad = ini[3]
        re = ini[4]
        le = ini[5]

        l1 = le
        g = Info(na,nu,pa,ad,re,l1)
        deposit(g,put)
        print("you deposited",put)
        #잔액 표시 기능 추가
    elif thing is 4:
        while True:
            account_num34 = input("input your account number")
            q = search_with_num(account_num34)
            if q is None:
                print("Your account number is not in our database")
            elif q is not None:
                break
        while True:
            account_pass34 = input("Enter your account password")
            q1 = search_with_pass(account_pass34)

            if q1 is None:
                print("Your password doesn't match your account number")#함수
            elif q1 is not None:
                break
        while True:
            ini_with = input("Input the amount you will withdraw")
            ini = search_data(account_num34,account_pass34)
            #print(ini)
            na = ini[0]
            nu = ini[1]
            pa = ini[2]
            ad = ini[3]
            re = ini[4]
            le = ini[5]
            g = Info(na,nu,pa,ad,re,le)
            g12 = withdraw(g,ini_with)
            print("g12 = ",g12)
            if g12 is None:
                print('THe amount you want to withdraw is larger than the money in your account')
            else:
                break
    elif thing is 5:
        print("Thank you. Please com again")
        #print("또 들려주세요 다음에도 ")
        #print("고객님의 편의를 위해 최선을 다하겠습니다")
        break
    else:
        print("Please check if you had inputted the right option above")