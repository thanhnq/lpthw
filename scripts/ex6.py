# assign the value of 10 to a variable called types_of_people
types_of_people = 10
# assign a value of a string to a variable called x
x = f"There are {types_of_people} types of people."

# assign two string values to two variables called binary and do_not
binary = "binary"
do_not = "don't"
# assign a string to a variable called y
y = f"Those who know {binary} and those who {do_not}."

# print two string x and y
print(x)
print(y)

# demonstrate a variable can hold a string
print(f"I said: {x}")
print(f"I also said: '{y}'")

# placement in a string
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# format a string with placement to be replaced with a value of a variable
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
