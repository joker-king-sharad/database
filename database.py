import mysql.connector
host=str(input("Enter server   : "))
user=str(input("Enter username : "))
passw=str(input("Enter password: "))
mydb =mysql.connector.connect(
    host=host,
    user=user,
    passwd=passw
)

def createDB(dataa):
    cur=mydb.cursor()
    q="create database "+dataa
    # print(q)
    cur.execute(q)
def showDB():
    cur=mydb.cursor()
    cur.execute("show databases")
    for x in cur:
        print(x)
def delDB(dataa):
    try:
        cur=mydb.cursor()
        cur.execute("drop database "+dataa)
    except Traceback :
        print("Not Exist")

def searDB(dataa):
    cur=mydb.cursor()
    cur.execute("show databases")
    for x in cur:
        if(x=='('+dataa+',)'):
            print("IS avalible")


def l():
    print("***********************************************\n")
def showAll():
    l()
    print("1.Create Database\n")
    print("2.Drop database \n")
    print("3.show database\n")
    print("4.find database\n")
    l()    
    num=int(input("Enter Your selection: "))
    if(num==1):
        dbb=str(input("Database Name: "))
        createDB(dbb)
    if(num==2):
        dbb=str(input("Database Name: "))
        delDB(dbb)

    if(num==3):
        showDB()
    if(num==4):
        dbb=str(input("Database Name: "))
        searDB(dbb)
        
    if(4<num):
        print("Wrong Number") 
        showAll()
    if(num==0):
        print("Wrong Number") 
        showAll()       

showAll()


    

