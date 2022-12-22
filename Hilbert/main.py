from turtle import *
from time import sleep

speed(0)
up()
setpos(-800, 0)
down()


def main():
    draw_qt1(3)


def draw_qt1(till=5):
    seqn = generate_sequence(till)
    print(seqn)
    for char in seqn:
        if char == "=":
            forward(10)
        elif char == "+":
            left(90)
        else:
            right(90)
    sleep(10000)


def generate_sequence(till=5, current="="):
    repl = "=-=-=+==+=+=-=-=+=+==+=-=-="
    for i in range(till):
        fin = ""
        i = 0
        while i < len(current):
            if current[i] == "=":
                fin += repl
            else:
                fin += current[i]
            i += 1
        current = fin
    return current


if __name__ == "__main__":
    main()
