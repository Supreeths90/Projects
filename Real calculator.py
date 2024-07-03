def calc(a,sy,b):
  if sy =="+":
    return a+b
  elif sy =="-":
    return a-b
  elif sy =="*":
    return a*b
  elif sy =="/":
    if a!=0 or b!=0:
        return a/b
    else:
      print("Zero div error")
  else:
    print("Invalid operator")

a = int(input("Enter a: "))
sy = input("Enter operator (+, -, *, /): ")
b = int(input("Enter b: "))

result = calc(a, sy, b)
if result is not None:
    print(result)

while True:
  sy = input("Enter operator (+, -, *, /) or 'q' to quit: ")
  if sy.lower() == 'q':
      break
  b = int(input("Enter b: "))

  result = calc(result, sy, b)
  if result is not None:
      print(result)
  else:
      break

  