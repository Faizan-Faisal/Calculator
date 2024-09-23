def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    if(num1 == 0 or num2 ==0):
        return 0
    else:
     return num1 * num2

def divide(num1, num2):
    if(num1 == 0):
        return 0
    elif(num2 == 0):
        return "Invalid - Math Error"
    else:
     return num1 / num2
    
num1 = float(input("Enter Number 1: "))
num2 = float(input("Enter Number 2: "))
calculation = input("Select Operation(+ , - , x , /): ")

if calculation == "+":
  print("Result: ", add(num1,num2))
elif calculation == "-" :
  print("Result: ", subtract(num1,num2))
elif calculation == "x" :
  print("Result: ", multiply(num1,num2))
elif calculation == "/":
  print("Result: ", divide(num1,num2))
else:
   print("Invalid statement selected")