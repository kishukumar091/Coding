class computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
    def setMaxPrice(self, price):
        self.__maxprice = price

c=computer()
c.sell()

c.__maxprice = 1000 # It can't Change the price because of private modifier
c.sell()

c.setMaxPrice(1000)
c.sell()


# In encapsulation It help us to hide the data
# we can't access the data directly