from turtle import *

color("green", "purple")
begin_fill()

wn = Screen()
canvas = getcanvas()


def main():
    generate_fibcurve(20)


def generate_fibcurve(till=35):
    fibstr = generate_fibonacci(till)  # a fibonacci string
    speed(0)
    up()
    setpos(-450, -375)
    down()
    wn.tracer(0)
    for i, char in enumerate(fibstr):
        if char == "0":
            if i % 2 == 1:
                right(90)
            else:
                left(90)
        forward(1)
    wn.update()
    canvas.postscript(file="fibonaccifractal.ps")
    input("")


def generate_fibonacci(till=10, previous="0", current="01"):
    print(till)
    if not till:
        return current
    return generate_fibonacci(
        till - 1,
        previous=current,
        current=current + compute_fib(current[len(previous) :]),
    )


def compute_fib(string):
    fin = ""
    for char in string:
        if char == "0":
            fin += "01"
        else:
            fin += "0"
    return fin


if __name__ == "__main__":
    main()
