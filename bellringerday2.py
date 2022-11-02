coffee_prices = [(
  'cappucino',
  1.5,
), ('expresso', 1.2), ('mocha', 1.9)]
expresso = 1.2
mocha = 1.9
cappucino = 1.5
highest_price = 0
#retrieve the coffee names and prices and price from the above tuple
for coffee, price in coffee_prices:
  print(f"coffee type {coffee} and price {price}")
# create a function for retrieving the highest priced
# def most_expensive_coffee(price,highest_price): ours
#   highest_price = 0
#   for coffee, price in coffee_prices:
#      if price > highest_price:
#        return highest_price


def my_most_expensive_coffee(coffee_prices):
  highest_price = 0
  my_most_expensive_coffee = ''
  for coffee, price in coffee_prices:
    if price > highest_price:
      highest_price = price
      my_most_expensive_coffee = coffee
    else:
      pass
  return (my_most_expensive_coffee, highest_price)


print(my_most_expensive_coffee(coffee_prices))


