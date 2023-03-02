


def square():
    new_value = 4 ** 2
    print(new_value)

square()
square()
square()

print("----")

def square(number):
    new_value = number ** 2
    print(new_value)

square(2)
square(3)
square(4)

print("----")

def square(number):
    new_value = number ** 2
    return new_value

for i in range(2, 8):
    result = square(number-i)

#result = square(2)
#print(result)
#result = square(3)
#print(result)
#result = square(4)
#print(result)

