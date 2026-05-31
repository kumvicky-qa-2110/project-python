# match case type code 

a = int(input("enter a drow number between 1 to 10 : "))

match a:
    case 1:
        print("you have won a car")
    case 5:
        print("you won a bike")
    case 10:
        print("you won a laptop")
    case _:
        print("sorry next time")


print("end of program one ")

b = int(input("enteryour api response code:"))

match b:
    case 200:
        print("passed")
    case 400:
        print("bad request")
    case 500:
        print("internal server error")
    case _:
        print("unknown error")


print ("end of program two")



        
            

