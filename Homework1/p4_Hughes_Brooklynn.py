import math
import matplotlib.pyplot as plt

def plot_function(fun_str, domain, ns):
    xs = []
    ys = []

    xmin = domain[0]
    xmax = domain[1]

    dx = (xmax - xmin) / (ns-1)
    x = xmin

    for i in range(ns):
        xs.append(x)

        y = eval(fun_str)

        ys.append(y)

        x = x + dx

    print()
    print("{:>10} {:>10}".format("x", "y"))
    print("----------------------")

    for i in range(ns):
        print("{:>10.4f} {:>10.4f}".format(xs[i], ys[i]))

    plt.plot(xs, ys, "bo-")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(fun_str)
    plt.grid(True)
    plt.show()

fun_str = input("Enter function with variable x: ")

ns = int(input("Enter number of samples: "))

xmin = float(input("Enter xmin: "))
xmax = float(input("Enter xmax: "))

plot_function(fun_str, (xmin, xmax), ns)
