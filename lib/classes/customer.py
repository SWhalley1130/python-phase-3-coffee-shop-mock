from classes.order import Order

class Customer:
    def __init__(self, name : str):
        self._name=name
        self.myorders=[]
        self.mycoffees=[]

    def get_name(self):
        return self._name
    
    def set_name(self,name):
        if type(name) is not str: 
            raise Exception("Please enter a string")
        if isinstance(name, str) and len(name)>0 and len(name)<16:
            self._name=name

    name=property(get_name, set_name)

    def orders(self):
        return self.myorders
    
    def coffees(self):
        return list(set(self.mycoffees))
    
    def create_order(self,coffee, price):
        return Order(self, coffee, price)

