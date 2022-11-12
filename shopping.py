product1 = input("what is product1 ")
product2 = input("what is product2 ")
product3 = input("what is product3 ")


price1 = float(input("what is the price of product1 "))
price2 = float(input("what is the price of product2 "))
price3 = float(input("what is the price of product3 "))

total = price1 + price2 + price3

average = round(total / 3,2)

print(f"the total of {product1}, {product2}, {product3} is R{total} and the average price of the items is R{average}")


