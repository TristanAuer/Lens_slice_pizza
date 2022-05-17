#list of pizza toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
#list of prices of pizza
prices = [2, 6, 1, 3, 2, 7, 2]
#number of repeating 2 price of pizza
num_two_dollar_slices = prices.count(2)
#length of topping list
num_pizzas = len(toppings)

print("We Sell", num_pizzas, "different kinds of pizza!")
#combine 2 lists (toppings, Prices) to a two-Dimeensional list
# https://docs.python.org/3.4/library/functions.html#zip resource
pizza_and_prices = list(zip(prices, toppings))
#sort by price
pizza_and_prices.sort()
#first element in pizza_and_prices in cheapest_pizza variable
cheapest_pizza = pizza_and_prices[0]
print("cheapest pizza",cheapest_pizza)
#Last element in pizza_and_prices in priciest_pizza variable
priciest_pizza = pizza_and_prices[-1]
print("priciest pizza", priciest_pizza)
#remove last item on pizza_and_prices list
pizza_and_prices.pop()
#updated list
priciest_pizza = pizza_and_prices[-1]
print("ran out new priciest pizza", priciest_pizza)
#list cheapest 3 pizzas in list
three_cheapest = pizza_and_prices[:3]
print("cheapest 3", three_cheapest)
'''for i in range(len(toppings)):
    for j in range(len(prices)):
        pizza_and_prices.append = [[i, j]]'''
print("list of all remaining pizza", pizza_and_prices)

'''print(num_pizzas)
print(num_two_dollar_slices)
print(toppings)'''