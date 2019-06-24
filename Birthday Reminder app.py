dict = {}
while 1:
    print("_______BIRTHDAY APP_______")
    print("1. Show Birthday")
    print("2. Add to birthday list")
    print("3. Exit")
    choose = int(input("Enter your choice"))
    if choose == 1:
        if(len(dict.keys())==0):
            print("Nothing To Show")
        else:
            name = input("Enter name to look for birthday")
            date= dict.get(name,"No data found")
            print(date)
    elif (choose==2):
        name= input("Enter friend's name")
        date= input("Enter Birthday")
        dict[name]=date
        print("Birthday Added")
    elif(choose==3):
        break
    else:
        print("Choose a valid option")