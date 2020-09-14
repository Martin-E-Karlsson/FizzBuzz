def main():
    fizzbuzz1(1, 100)


def fizzbuzz1(lower_limit, upper_limit):
    for i in range(lower_limit, upper_limit + 1):
        message = ""
        if i % 3 == 0 and (i == 42) is False:
            message = message + "Fizz"
        if i % 5 == 0:
            message = message + "Buzz"
        if message == "":
            message = i
        if i == 42:
            print("Answer to the Ultimate Question of Life, the Universe, and Everything")
        elif (i == 42) is False:
            print(message) #test för att se om collaboration funkar


def fizzbuzz2(lower_limit, upper_limit):
    for i in range(lower_limit, upper_limit):
        pass


if __name__ == "__main__":
    main()
