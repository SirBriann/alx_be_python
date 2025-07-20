num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        add_result = num1 + num2
        print(f"The result is {add_result}")
    case "-":
        sub_result = num1 - num2
        print(f"The result is {sub_result}")
    case "*":
        mult_result = num1 * num2
        print(f"The result is {mult_result}")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            div_result = num1 / num2
            print(f"The result is {div_result}")
    case _:
        print("Invalid operation. Please choose +, -, *, or /.")


