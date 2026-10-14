cbook={}


while(True):

    print("Welcome to the contact Book ")
    print("Options")
    print("1.Add Content ")
    print("2.Search content")
    print("3.Update content")
    print("4.Delete content")
    print("5.Display contents")
    print("6.Exit")
    print()

    
    choice = int(input("enter the choice from above...  : "))


   
    if(choice == 1):
        name=input("Enter the name to add : ")
        value= input("enter the value to add : ")

        cbook[name] = value
    elif(choice == 2):
        name=input("Enter the name to search : ")

        if name in cbook:
            print("Found : " , cbook[name])
        else:
            print("Not found ")
    elif(choice == 3):
        name=input("Enter the name to update : ")
        value=input("Enter the value to update  : ")

        if name in cbook:
            cbook[name] = value
            print("Updated Successfully")
        else:
            print("Not Found ")
    elif(choice == 4):
         name= input("Enter the name to delete : ")

         if name in cbook:
             del cbook[name]
             print("Successfully deleted ")
         else:
             print("Not Found ")
    elif(choice == 5):
        for i in cbook:
            print(i , " : " , cbook[i])
    elif(choice == 6):
        print("Exiting.. Thank You")
        break;
    else:
        print("Invalid Input " )
        
