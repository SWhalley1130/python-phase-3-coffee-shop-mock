#!/usr/bin/env python3
import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    #ipdb.set_trace()


mocha=Coffee("Mocha")
cap=Coffee("Cap")

sarah=Customer("Sarah")
lewie=Customer("Lewie")
ex=Customer("Example")

o1=Order(sarah, cap, 4)
o2=Order(lewie, cap, 3)
o3=Order(sarah, cap, 3)




