def main():
    for i in range(1, 101):
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
            print(message)


if __name__ == "__main__":
    main()
