
def grading():
  a = input("Enter your full name: ")
  b = int(input(" Enter your marks: "))
  if b>=80 and b<=100:
    print("You got an A")
  elif b>=70 and b<=79:
    print("You got B grade")
  elif b>=60 and b<=69:
    print("You got C grade")
  elif b>=50 and b<=59:
    print("You got D grade")
  elif b<50:
    print("You got F grade")
  else:
    print("Invalid!!!")
grading()