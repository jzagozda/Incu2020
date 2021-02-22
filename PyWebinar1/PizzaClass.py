class Pizza:
    def _init_(self, diameter, pizza_type, base_sauce):
        self.diamater = diameter
        self.pizza_type = pizza_type
        self.base_sauce = base_sauce
  
vege_pizza = Pizza()
vege_pizza.diameter = 50
vege_pizza.pizza_type = "Quattro Fromaggi"
vege_pizza.base_sauce = "Olive oil"


simple_pizza = Pizza()
vege_pizza.diameter = 32
vege_pizza.pizza_type = "Prosciutto"
vege_pizza.base_sauce = "Garlic sauce"

base_pizza = Pizza()
base_pizza.diameter = 40
base_pizza.pizza_type = "Margheritta"
base_pizza.base_sauce = "Tomato sauce"
