#no graphical user interface

deg = int(input("Enter the degree of the polynomial: "))

print("""Enter the coefficients of the polynomial in decreasing order of degree such as
      a*x^2 + b*x + c = 0""")

a = float(input('a='))
b = float(input('b='))
c = float(input('c='))

delta = b**2 - 4*a*c

def solve_quadratic(a, b, c):
    if delta > 0 :
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        return x1, x2
    elif delta == 0:
        x = -b / (2*a)
        return x,
    else:
        print('no real roots')