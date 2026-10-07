def add_and_print(a, b):
    print(a + b)


def add_and_return(a, b):
    return a + b


add_and_print(2, 3)
add_and_return(2, 3)

first = add_and_print(10, 5)
second = add_and_return(10, 5)

print(first)
print(second)

print(add_and_return(2, 3) * 10)

def add_and_print(a, b):
    print(a + b)
    return a + b
