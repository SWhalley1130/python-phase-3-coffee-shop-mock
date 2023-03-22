from classes.order import Order

class Coffee:
    def __init__(self, name):
        if type(name) is str: 
            self._name=name
        self.myorders=[]
        self.mycustomers=[]
    
    def get_name(self):
        return self._name
    
    def set_name(self,name):
        print("Cannot change name.")

    name=property(get_name,set_name)

    def orders(self):
        return self.myorders
    
    def customers(self):
        return list(set(self.mycustomers))
    
    def num_orders(self):
        return len(self.myorders)
    
    def average_price(self):
        sum=0
        for coffee in self.myorders:
            sum+=coffee.price
        return sum/len(self.myorders)
    
    def delete(self):
        del self