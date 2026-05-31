num1 = int(input("enter a number: "))
num2 = int(input("enter another number: "))
opr = input("enter an operator: ")  

match opr:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
    case _:
        print("Invalid operator")

        