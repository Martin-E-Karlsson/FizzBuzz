def main():
    for i in range(1, 101): #problem 1: här printas inte 1 ut, väljer jag range mellan 0 och 100 så printas "fizz" buzz också ut då 5 / 0 blir 0 i pythons värld.
        if i % 3 == 0:
            print('Fizz')
        if i % 5 == 0:
            print('Buzz')
        if i % 5 == 0 and i % 3 == 0:
            print("Fizzbuzz")
        if i == 42:
            print("Answer to the Ultimate Question of Life, the Universe, and Everything")
        else:
            print(i) #problem 2: här printas siffran 42 ut som ska vara ersatt av "answer to the...." jobbar på att göra något form av undantag då 42/3=14 så printas dessutom "fizz" ut


if __name__ == "__main__":
    main()
 
