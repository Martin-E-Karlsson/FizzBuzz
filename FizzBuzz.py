def main():
    for i in range(1, 101):
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


if __name__ == "__main__":
    main()
