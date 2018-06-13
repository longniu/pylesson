# Goods class

class goods :
    # init method
    def __init__(self, name, price):
        self.__data = {"name":name, "price":price}

    '''
    The default way to defined getter and setter
    # name property getter
    @property
    def name(self):
        return self.__data["name"]

    # name property setter
    @name.setter
    def name(self, value):
        self.__data["name"] = value

    # price property getter
    @property
    def price(self):
        price = self.__data["price"]
        price_str = f"{price:,} dollar"
        return price_str
    '''

    '''
    define getter and setter by self defined method name
    use property() method to point which method is getter or setter
    '''
    # name property getter
    def get_name(self):
        return self.__data["name"]

    # name property setter
    def set_name(self, value):
        self.__data["name"] = value

    # price property getter
    def get_price(self):
        price = self.__data["price"]
        price_str = f"{price:,} dollar"
        return price_str

    # select property
    name = property(get_name, set_name)
    price = property(get_price)
