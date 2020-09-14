def main():
    # fizzbuzz1(1, 100)
    fizzbuzz2(1, 100)


def fizzbuzz1(lower_limit, upper_limit):
    for i in range(lower_limit, upper_limit + 1):
        x = ""
        if i % 3 == 0 and (i == 42) is False:
            x = x + "Fizz"
        if i % 5 == 0:
            x = x + "Buzz"
        if x == "":
            x = i
        if i == 42:
            print("Answer to the Ultimate Question of Life, the Universe, and Everything")
        elif (i == 42) is False:
            print(x)


def fizzbuzz2(lower_limit, upper_limit):
    for number in range(lower_limit, upper_limit + 1):
        if number == 42:
            print("Answer to the Ultimate Question of Life, the Universe, and Everything", end="")
        else:
            if number % 3 == 0:
                print("Fizz", end="")
            if number % 5 == 0:
                print("Buzz", end="")
            if number % 3 != 0 and number % 5 != 0:
                print(number, end="")
        print()


if __name__ == "__main__":
    main()
