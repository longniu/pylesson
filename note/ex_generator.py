
# create a generator with number list
def num_generator() :
    n = 0
    while True:
num = n*n + 2*n + 3
        yield num
        n += 1

# do something in the function
def do_something(num):
    return (num%2, num%3)

# operate item taken from generator
gen = num_generator()
for i in range(1, 10):
    num = next(gen)
    result = do_something(num)
    print(result)

'''
Create Fizz Buzz game
'''
# Create Fizz Buzz generator
def fizzbuzz():
    n = 1
    while True:
        if n%15 == 0:
            yield 'FizzBuzz'
        elif n%3 == 0:
            yield 'Fizz'
        elif n%5 == 0:
            yield 'Buzz'
        else :
            yield str(n)
        n += 1

# Create a game generator by fizzbuzz() and call 20 rounds
game = fizzbuzz()
for x in range(0,20):
    print(next(game))

