import math
import matplotlib.pyplot as plt

while True:
    a = input("Enter a: ")

    if a == "":
         break



    a = float(a)
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        print("no real solutions")

        xopt = -b/(2*a)
        xmin = xopt - 5
        xmax = xopt + 5

    elif discriminant == 0:
        root = -b/(2*a)
        print("one solution:", root)

        xmin = root - 2
        xmax = root + 2

    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print("two solutions:", root1, root2)

        xmin = min(root1, root2) - 2
        xmax = min(root1, root2) + 2

    xs = []
    ys = []

    n = 150
    dx = (xmax - xmin) / n

    x = xmin
    
    while x <= xmax:
        xs.append(x)
    
        y = a * x**2 + b * x + c
        ys.append(y)
    
        x += dx

    plt.figure()
    plt.plot(xs, ys)
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    plt.grid(True)
    plt.title("y = ax² + bx + c")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    
        
