
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
op = input("Enter operator (+ , - , * or /) :")
def cal():
  if op == "+":
    print("Sum of the numbers is:", x + y)
  elif op == "-":
    print("Difference of the numbers is:", x - y)
  elif op == "*":
    print("Product of the numbers is:", x * y)
  elif op == "/":
    if y == 0:
      print("\t Error: Dividing by zero gives infinity!")
    else:
      print("Division of the numbers is:", x / y)
cal()