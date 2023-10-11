def pizza_toppings(cheese_type, sausage_type, pepper_type):
    print(f"We can have a pizza party with \n Cheeses:{cheese_type} \n Sausages: {sausage_type} \n Peppers: {pepper_type}")

def pizza_topping_count(cheese_count, sausage_count,pepper_count):
    print(f"We have: \n -{cheese_count} cheeses \n -{sausage_count} sausages \n -{pepper_count} peppers")

def total_pizza(cheese_pizza_count):
    print(f"We have {int(cheese_pizza_count)} cheese pizzas remaining.")

cheese = ("Mozzerela", "Colby")
sausage = ("Mild", "Spicy")
peppers = ("Green", "Red", "Yellow")

pizza_toppings(cheese, sausage, peppers)

cheese_count = 100
sausage_count = 30
pepper_count = 30
pizza_topping_count(cheese_count, sausage_count, pepper_count)

cheese_per_pizza = 5
sausage_per_pizza = 2
pepper_per_pizza = 1

total_pizza(cheese_count / cheese_per_pizza) 
          
    