def generate_fibonacci(till=10, previous="0", current="01"):
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


print(generate_fibonacci())
