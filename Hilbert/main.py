from turtle import *
from time import sleep

speed(0)
up()
setpos(-800,0)
down()
def main():
    draw_qt1(5)

def draw_qt1(till=5):
    seqn = generate_sequence(till)
    print(seqn)
    for char in seqn:
        if char=='=':
            forward(10)
        elif char=='+':
            left(90)
        else:
            right(90)

def generate_sequence (till=5,current='-=+=+='):
    repl='=-=-=+==+=+=-=-=+=+==+=-=-='
    replacable=['=-=-=',
    '=+=+=',
    '=-=+=',
    '=+=-=',
    ]
    for i in range(till):
        fin=''
        i=0
        while i < len(current):
            print(current[i:i+5])
            if current[i:i+5] in replacable:
                print('True')
                fin+=repl
                i+=4
            else:
                fin += current[i]
            i+=1
        current=fin
    return current

if __name__ == '__main__':
    main()
