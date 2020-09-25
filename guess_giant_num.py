import random

y = 10000
while y > 1000:
    y = int(input("# of digits\n"))
x = random.randint(10 ** (y-1), 10 ** y)
print("0" * y)

while True:
    y = input("Guess\n")
    try:
        if y[-1] == "c":
            for i in range(len(y) - 2, 0, -1):
                if y[i] != "0":
                    print(i+1)
                    break
        elif y.lower() == "quit":
            print(x)
            break
        elif int(y) == x:
            break
        elif len(y) != len(str(x)):
            print("Wrong number of digits")
        elif int(y) > x:
            print("Too high")
        elif int(y) < x:
            print("Too low")

    except:
        print("Error")
        continue
