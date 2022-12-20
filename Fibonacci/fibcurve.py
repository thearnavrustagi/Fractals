from turtle import *
color('green','purple')
begin_fill()

def main ():
    generate_fibcurve(15)

def generate_fibcurve(till=35):
    fibstr = generate_fibonacci(till) # a fibonacci string
    speed(0)
    up()
    setpos(-800,-400)
    down()
    for i,char in enumerate(fibstr):
        if char == '0':
            if i%2 == 1:
                right(90)
            else:
                left(90)
        forward(2)

def generate_fibonacci (till=10,previous='0',current='01'):
    print(till)
    if not till: return current
    return generate_fibonacci(
            till-1,
            previous=current,
            current=current+compute_fib(current[len(previous):]))

def compute_fib (string):
    fin = ''
    for char in string:
        if char == '0':
            fin+='01'
        else:
            fin+='0'
    return fin

if __name__ == '__main__':
    main()

