from turtle import *
from time import sleep

speed(0)
up()
setpos(-800,-400)
down()
def main():
    draw_qt1(5)

def draw_qt1(till=5):
    seqn = generate_sequence(till)
    print(seqn)
    for char in seqn:
        if char=='=':
            forward(5)
        elif char=='+':
            left(90)
        else:
            right(90)

def generate_sequence (till=5,current='='):
    repl='=+=-=-==+=+=-='
    for i in range(till):
        fin=''
        for char in current:
            if char == '=':
                fin+=repl
            else:
                fin+=char
        current=fin
        print(current)
    return current

if __name__ == '__main__':
    main()
