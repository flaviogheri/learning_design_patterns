
class Burger: 

    def __init__(self): 
        self.meat_type = None
        self.toppings = None
        self.cooking_level = None

    def list_parts(self): 
        return f"Meat: {self.meat_type}, Toppings: {', '.join(self.toppings)}, Cooking Level: {self.cooking_level}"

class Steak:

    def __init__(self):
        self.meat_type = None 
        self.cooking_level = None
    
    def list_parts(self):
        return f"Steak: {self.meat_type} at {self.cooking_level}"



class Meal: 

    def __init__(self, main, drink, side): 

        self.main = main
        self.drink = drink
        self.side = side

    def list_parts(self): 
        # return f"Burger: {self.burger}, Drink: {self.drink}, Side: {self.side}"
        return f"Burger with:  {self.main.list_parts()}\nDrink: {self.drink}\nSide: {self.side}"



class MealBuilder(): 

    def __init__(self): 
        self.main = None
        self.drink = None
        self.side = None

    def set_main(self, main): 
        self.main = main
        return self
    
    def set_drink(self, drink): 
        self.drink = drink
        return self

    def set_side(self, side): 
        self.side = side
        return self
    
    def build(self): 
        return Meal(self.main, self.drink, self.side)

# Concrete Builder #1
class ClassicBurger(Burger): 

    def __init__(self): 
        super().__init__()
        self.meat_type = "beef"
        self.toppings = ["lettuce"]
        self.cooking_level = "well done"

# Overriding + Inheritance example
class CheeseBurger(ClassicBurger): 
    
    def __init__(self): 
        super().__init__()
        self.toppings.append("cheese")

class AmericanBurger(CheeseBurger): 
    
    def __init__(self): 
        super().__init__()
        self.toppings.extend(["bacon", "bbq sauce"])

# Concrete Builder #2
class WagyuSteak(Steak):

    def __init__(self): 
        super().__init__()
        self.meat_type = "Wagyu"
        self.cooking_level = "rare"



if __name__=='__main__': 

    builder  = MealBuilder()

    order = (builder.set_main(AmericanBurger())
                   .set_drink("soda")
                   .set_side("chips")
                   .build())

    print(order.list_parts())

    order = (builder.set_main(WagyuSteak())
                   .set_drink("soda")
                   .set_side("chips")
                   .build())

    print(order.list_parts())

