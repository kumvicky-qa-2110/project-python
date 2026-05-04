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

        
            

