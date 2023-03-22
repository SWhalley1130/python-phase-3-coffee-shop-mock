
class Order:

    all=[]

    def __init__(self, customer, coffee, price):
        from .customer import Customer
        from .coffee import Coffee
        if isinstance(customer, Customer):   
            self.customer=customer
        if isinstance(coffee,Coffee):
            self.coffee=coffee
        if isinstance(price, int) and price>0 and price<11:
            self.price=price

        Order.all.append(self)

        coffee.myorders.append(self)
        coffee.mycustomers.append(self.customer)

        customer.myorders.append(self)
        customer.mycoffees.append(self.coffee)

    def get_all_orders(self):
        return Order.all