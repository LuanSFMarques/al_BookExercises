#Write a fizzBuzz() function with a single integer parameter named upTo. For the numbers 1
#up to and including upTo, the function prints one of four things:
#-- Prints 'FizzBuzz' if the number is divisible by 3 and 5.
#-- Prints 'Fizz' if the number is only divisible by 3.
#-- Prints 'Buzz' if the number is only divisible by 5.
#-- Prints the number if the number is neither divisible by 3 nor 5.

#Finished!
def fizzBuzz(upTo):
    x = 1
    while x<=upTo:
        if x % 15 == 0:                             #multiplo de 3 e de 5, mmc
            print ('FizzBuzz', end='')
        elif x % 3 == 0:
            print ('Fizz', end='')
        elif x % 5 == 0:
            print ('Buzz', end='')
        else:
            print (str(x), end='')
        print(" ", end='')
        x = x + 1
    return ""
print (fizzBuzz(31))