import random 

def random_num():
    a = int(input("Type Minimum: "))
    b = int(input("Type Maximum: "))

    numbers = [random.randint(a, b) for i in range(1)] # Change this number to what you want to get more outputs.
    print(','.join(str(n) for n in numbers))

random_num()
