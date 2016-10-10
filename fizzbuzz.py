

guess = int(raw_input("Select a number between 1 and 100: "))

if guess > 100:
    print "Your number is bigger than 100. Try again!"
elif guess < 1:
    print "Your number is smaller than 1. Try again!"
else:
    for number in xrange(1,guess+1):
        if (number % 15) == 0:
            number = "fizzbuzz"
        elif (number % 3) == 0:
            number = "buzz"
        elif (number % 5) == 0:
            number = "fizz"

        print (number)


