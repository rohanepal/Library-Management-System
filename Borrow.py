import dt       
import ListSplit

def borrowBook():
    success=False 
    while(True):       #entering details of burrower
        firstName=input("Enter the first name of the borrower: ") 
        if firstName.isalpha():
            break
        print("please input alphabet from A-Z")
    while(True):
        lastName=input("Enter the last name of the borrower: ")
        if lastName.isalpha():
            break
        print("please input alphabet from A-Z")
            
    t="Borrow-"+firstName+".txt"   # creating Burrower txt file
    with open(t,"w+") as f:                                      
        f.write("               Library Management System  \n")     #writting datails for Burrower txt file
        f.write("                   Borrowed By: "+ firstName+" "+lastName+"\n")
        f.write("    Date: " + dt.getDate()+"    Time:"+ dt.getTime()+"\n\n")
        f.write("S.N. \t\t Bookname \t      Authorname \n" )
    
    while success==False:
        print("Please select a option below:")        #conforming book burrowing 
        for i in range(len(ListSplit.bookname)):
            print("Enter", i, "to borrow book", ListSplit.bookname[i])
    
        try:   
            a=int(input())
            try:
                if(int(ListSplit.quantity[a])>0):
                    print("Book is available")
                    with open(t,"a") as f:
                        f.write("1. \t\t"+ ListSplit.bookname[a]+"\t\t  "+ListSplit.authorname[a]+"\n")

                    ListSplit.quantity[a]=int(ListSplit.quantity[a])-1 #deducting from stock
                    with open("Stock.txt","w+") as f:
                        for i in range(3):
                            f.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+"$"+ListSplit.cost[i]+"\n") #updating stock


                    #multiple book borrowing code
                    loop=True
                    count=1
                    while loop==True:
                        choice=str(input("Do you want to borrow more books? However you cannot borrow same book twice. Press y for yes and n for no."))
                        if(choice.upper()=="Y"):
                            count=count+1                                #increasing number of book been burrowed
                            print("Please select an option below:")
                            for i in range(len(ListSplit.bookname)):
                                print("Enter", i, "to borrow book", ListSplit.bookname[i])
                            a=int(input())
                            if(int(ListSplit.quantity[a])>0):
                                print("Book is available")
                                with open(t,"a") as f:
                                    f.write(str(count) +". \t\t"+ ListSplit.bookname[a]+"\t\t  "+ListSplit.authorname[a]+"\n")

                                ListSplit.quantity[a]=int(ListSplit.quantity[a])-1    #deducting from stock
                                with open("Stock.txt","w+") as f:
                                    for i in range(3):
                                        f.write(ListSplit.bookname[i]+","+ListSplit.authorname[i]+","+str(ListSplit.quantity[i])+","+"$"+ListSplit.cost[i]+"\n")     #updating stock
                                        success=False
                            else:
                                loop=False
                                break
                        elif (choice.upper()=="N"):
                            print ("Thank you for borrowing books from us. ")
                            print("")
                            loop=False
                            success=True
                        else:
                            print("Please choose as instructed")
                        
                else:
                    print("Book is not available")
                    borrowBook()
                    success=False
            except IndexError:
                print("")
                print("Please choose book acording to their number.")
        except ValueError:
            print("")
            print("Please choose as suggested.")
