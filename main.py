from numpy import sqrt
print("You have an equation ax^2+bx+c = 0")
print("Enter the coefficients for a, b, c")

while 1:
  try:
    a=int(raw_input("a = "))
    break
  except ValueError:
    print("Enter a number")
    continue
  
while 1:
  try:
    b=int(raw_input("b = "))
    break
  except ValueError:
    print("Enter a number")
    continue

while 1:
  try:
    c=int(raw_input("c = "))
    break
  except ValueError:
    print("Enter a number")
    continue
  

if a==0:
  print("Not a quadratic equation")
  if b==0:
    print("There is no x")
  else:
    x1=-b/c
    print("x1 = "+str(x1))
else:
  if b**2-4*a*c<0:
    print("No Real Roots")
  else:
    x1=(-b+sqrt(b**2-4*a*c))/(2*a)
    x2=(-b-sqrt(b**2-4*a*c))/(2*a)
    print("x1 = "+str(x1))
    print("x2 = "+str(x2))



