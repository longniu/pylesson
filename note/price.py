# define a closer
def charge(price) :
    def calc(num):
        return price * num
    return calc

# new 2 closers
child = charge(400)
adult = charge(1000)

price1 = child(3)
price2 = adult(2)

print(price1)
print(price2)
