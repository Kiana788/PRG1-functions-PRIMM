def double_it(number):
    number = number * 2
    return number


value = 5
result = double_it(value)

print(value)
print(result)


message = "outside"


def show_message():
    message = "inside"
    print(message)


show_message()
print(message)

def show_message(text):
    print(text)


show_message("outside")
show_message("anything at all")
