print("I have a class of 33 students.")
print("there are 11 girls, so that means...")
print()
#In this line, there is an f string and numbers inside that calculate the percentage of girls in the class.
#The round() function rounds the percentage to 2 decimal places as it is a repeating decimal.
print(f"that means {round(11/33, 2)}% are girls")
#The use of .format() directly injects the numbers calculated (the percentage of boys in the class)
#The round() function rounds the percentage to 2 decimal places.
print("and {}% are boys.".format(round((33-11)/33), 2))
print()
print("If we made groups of six...")
#The f sting allows for the numbers to be in the string
# // is floor division, which means that it rounds the result down to the nearest whole number.
print(f"there would be {33//6} groups of six")
# % is modulus, which means that it gives the remainder after dividing 33 by 6
(f"and if there needed to be smaller groups of {33%6} people.")
# this line prints "-" 30 times
print("-" * 30)
print("If we had 17 apples and 3 people...")
#The use of floor division rounds the result of 17/3 down to the nearest whole number.
print(f"Each person would get {17//3} whole apples")
#The use of concactenation and converting the integer(result from modulus which is the remainder of 17/3) into a string.
print("there would be" + str(17%3) + " apples remaining")
print()
print("if we charged each person $2 for their 5 apples...")
#The .format() injects 2*5 into the string.
print("they would each pay ${}.".format(2*5))