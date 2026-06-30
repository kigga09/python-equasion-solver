#no graphical user interface

deg = int(input("Enter the degree of the polynomial: "))

if deg == 1:
    print('enter the coefficients of the polynomial in the form ax + b = 0')
    a = float(input("a= "))
    b = float(input("b= "))
    if a == 0:
        print("error: coefficient a cannot be zero for a linear equation.")
    else:
       print(f"The solution to the equation is: x = {-b/a}")
elif deg == 2:
    print('enter the coefficients of the polynomial in the form ax^2 + bx + c = 0')
    a = float(input("a= "))
    b = float(input("b= "))
    c = float(input("c= "))
    if a == 0:
        print("error: coefficient a cannot be zero for a quadratic equation.")
    else:
        return 'No real roots'
