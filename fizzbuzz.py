def get_fizz_buzz_numbers():
    return(range(1, 101))

def fizz_buzz_calc(an_integer):
    if(an_integer == 15):
        return("FizzBuzz")
    if(an_integer % 3 == 0):
        return("Fizz")
    if(an_integer % 5 == 0):
        return("Buzz")
    else:
        return(an_integer)
