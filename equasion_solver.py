#no graphical user interface

print("This program solves polynomial equations of degree 1 and 2.")
deg = int(input("Enter the degree of the polynomial: "))

if deg == 1:
    print('enter the coefficients of the polynomial in the form ax + b = 0')
    a = float(input("Enter the coefficient a: "))
    b = float(input("Enter the coefficient b: "))
    if a == 0:
        print("error: coefficient a cannot be zero for a linear equation.")
    else:
       return b / a
elif deg == 2:
    print('enter the coefficients of the polynomial in the form ax^2 + bx + c = 0')
    a = float(input("Enter the coefficient a: "))
    b = float(input("Enter the coefficient b: "))
    c = float(input("Enter the coefficient c: "))
    if a == 0:
        print("error: coefficient a cannot be zero for a quadratic equation.")
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            print("The equation has no real roots.")
        elif delta == 0:
            root = -b / (2*a)
            print(f"The equation has one real root: {root}")
        else:
            root1 = (-b + delta**0.5) / (2*a)
            root2 = (-b - delta**0.5) / (2*a)
            print(f"The equation has two real roots: {root1} and {root2}")