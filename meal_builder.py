#!/usr/bin/env python3
"""
This code is a simple example of the Builder Design Pattern. Currently uses the builder method but doesnt take advantage
(only one meal is available) - therefore dont have inherently different functions if I understand this correctly ?...

Instead what uses effectively - Inheritance -> CheeseBurger etc.. inhereted other Burger types, of which add other topics

Another effective tool -> Overriding functions -> In order to print the contents, 
the classes that inhereted meal override it with their own elements.

@Author: Flavio Gheri
@Date: 26/09/24

"""
class Burger: 

    def __init__(self): 
        self.meat_type = None
        self.toppings = None
        self.cooking_level = None

    def list_parts(self): 
        return f"Meat: {self.meat_type}, Toppings: {', '.join(self.toppings)}, Cooking Level: {self.cooking_level}"


class Meal: 

    def __init__(self, burger, drink, side): 

        self.burger = burger
        self.drink = drink
        self.side = side

    def list_parts(self): 
        # return f"Burger: {self.burger}, Drink: {self.drink}, Side: {self.side}"
        return f"Burger with:  {self.burger.list_parts()}\nDrink: {self.drink}\nSide: {self.side}"



class MealBuilder(): 

    def __init__(self): 
        self.burger = None
        self.drink = None
        self.side = None

    def set_burger(self, burger:Burger): 
        self.burger = burger
        return self
    
    def set_drink(self, drink): 
        self.drink = drink
        return self

    def set_side(self, side): 
        self.side = side
        return self
    
    def build(self): 
        return Meal(self.burger, self.drink, self.side)


class ClassicBurger(Burger): 

    def __init__(self): 
        super().__init__()
        self.meat_type = "beef"
        self.toppings = ["lettuce"]
        self.cooking_level = "well done"


class CheeseBurger(ClassicBurger): 
    
    def __init__(self): 
        super().__init__()
        self.toppings.append("cheese")

class AmericanBurger(CheeseBurger): 
    
    def __init__(self): 
        super().__init__()
        self.toppings.extend(["bacon", "bbq sauce"])


if __name__=='__main__': 

    builder  = MealBuilder()

    order = (builder.set_burger(AmericanBurger())
                   .set_drink("soda")
                   .set_side("chips")
                   .build())

    print(order.list_parts())
