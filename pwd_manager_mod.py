import mysql.connector
from base64 import encode
from pickle import TRUE
from cryptography.fernet import Fernet
import os
os.system("cls")

def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

#write_key()

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

pass1 = "DBMS"
key1 = load_key()
fer = Fernet(key1)

pin = input("Enter Master Password: ")

def add():

    acc = input("Enter Account name : ")
    user = input("Enter Username : ")
    pwd = input("Enter password : ")
    cur.execute(f"insert into pwd values('{acc}','{fer.encrypt(user.encode()).decode()}','{fer.encrypt(pwd.encode()).decode()}');")
    my_db.commit()


def view():

    cur.execute("select * from pwd ;")
    rows=cur.fetchall()
    for row in rows:
        account,username,pwds=row
        print(" Account :",account.lower(),"\n","Username :",fer.decrypt(username.encode()).decode() ,
              "\n","Password :",fer.decrypt(pwds.encode()).decode(),"\n")
    
def update():

    view()
    acc=input("\nEnter the Account name you want to delete : ")
    user = input("Enter New Username : ")
    pwd = input("Enter New password : ")
    msg=cur.execute(f"update pwd set username='{fer.encrypt(user.encode()).decode()}',password='{fer.encrypt(pwd.encode()).decode()}' where account='{acc}';")
    my_db.commit()
    print(msg)

def delete():

    view()
    acc = input("\nEnter the Account name you want to delete : ")
    msg = cur.execute(f"delete from pwd where account='{acc}';")
    my_db.commit()
    print(msg)

if pin == pass1:

    os.system("cls")
    my_db=mysql.connector.connect(host="localhost",user="root",password="toor")
    cur=my_db.cursor()
    #cur.execute("create database passwords;")
    cur.execute("use passwords;")
    #cur.execute("create table pwd(account varchar(20),username varchar(256),password varchar(256))")
    my_db.commit()
    
    while True:

        #os.system("cls")
        mode = input('''\n\n\nPress 1 to add new Password.
                            \nPress 2 to view saved Passwords.
                            \nPress 3 to update saved Passwords.           
                            \nPress 4 to delete a Password.
                            \nPress 5 to quit\n\n---> ''')

        if mode == '1':
            os.system("cls")
            add()
        
        elif mode == '2':
            os.system("cls")
            view()   

        elif mode == '3':
            os.system("cls")
            update()

        elif mode == '4':
            os.system('cls')
            delete()

        elif mode == '5':
            os.system("cls")
            break
