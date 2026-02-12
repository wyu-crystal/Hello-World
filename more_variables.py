store = "No Frills"
item = "Apples"
price = 0.25
quantity = 8
subtotal = price * quantity
tax = subtotal * 0.05
total = tax + subtotal

#f-string
print(f"At {store} I bought some {item}.")
#concatenation
print("they sould for$" + str(price) + " each.")
#dot format
print("I wanted to purchase {} of them.".format(quantity))
#concatenation
print("The subtotal was $" + str(subtotal))
#f-string
print(f"The tax was ${round(tax, 2)}")
#f-string
print(f"The total price, with tax included, was ${total}.")

#The missing part in the last line is the f in the front of the quotation mark, for f string
