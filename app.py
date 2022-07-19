def init():
    operation = 0
    steps = []
    while operation != 5:
        number = int(input("Type number: "))
        operation = int(input("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Result\nOperation: "))
        steps.append(number)
        if operation > 5:
            print("Please choose correct operation")
            break
        elif operation == 1:
            steps.append("+")
        elif operation == 2:
            steps.append("-")
        elif operation == 3:
            steps.append("*")
        elif operation == 4:
           steps.append("/")
    else:

      return calculate(steps)
        


def calculate(steps):
    prevOperation = ""
    result = 0
    for element in steps:
        if prevOperation == "":
            result += element
            prevOperation = "x"
        elif type(element) == type(""):
            prevOperation = element
                
        elif type(element) == type(0) and prevOperation == "+":
            result += element
        elif type(element) == type(0) and prevOperation == "-":
            result -= element
        elif type(element) == type(0) and prevOperation == "*":
            result *= element
        elif type(element) == type(0) and prevOperation == "/":
            result /= element

    return print(f"{'#'*100}\nRESULT = {steps} = {result}\n{'#'*100}")
                                                

init()