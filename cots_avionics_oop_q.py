class MainItem:
    
    discount= 0.8
    
    def __init__(self, name: str, price: float):
        
        assert price >= 0, f"Price {price} cannnot be less than 0"
        
        self.name = name
        self.price = price 
        
    def discountedprice(self):
        return f"The discounted price of {self.name} is {self.price * self.discount}"

class Banana(MainItem):
    
    discount = 0.5

class Apple(MainItem):
    
    discount1 = 0.4
    
    def __init__(self, name, price, number=1): 
        super().__init__(name, price)
        self.number = number
    
    def discountedprice(self):
        if self.number >= 5:
            return f"The discounted price of {self.name} is {self.price * self.discount1}"
        else:
            return f"The discounted price of {self.name} is {self.price * self.discount}"

          
item1 = MainItem('Comb', 15)
item2 = Banana('Lady Finger', 20)
item3 = Apple('Green Apple', 24, 4)

item1.discountedprice()
item2.discountedprice()
item3.discountedprice()
