def get_fizz_buzz_numbers():
    return(list(map(fizz_buzz_calc, range(1, 101))))

def fizz_buzz_calc(an_integer):
    isFuzz = (an_integer % 3 == 0)
    isBuzz = (an_integer % 5 == 0)
    if(isFuzz and isBuzz):
        return("FizzBuzz")
    if(isFuzz):
        return("Fizz")
    if(isBuzz):
        return("Buzz")
    else:
        return(an_integer)
