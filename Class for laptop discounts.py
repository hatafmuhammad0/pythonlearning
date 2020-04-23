#Creating a function to apply laptop discount

class Laptop:
    def __init__ (self , name , model , price):
        self.name = name
        self.model = model
        self.price = price

    def discount(self, num):
        self.new_price = (100-num)/ 100 * self.price
        return self.new_price

laptop_1 = Laptop("Dell" , "Jx100" , 20000)
laptop_2 = Laptop(laptop_1.name , "Jx100" , 40000)

print(laptop_1.discount(40))
print(laptop_2.discount(50))