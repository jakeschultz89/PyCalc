# this is a comment

# variables
name = "Jake"
age = 31
price = 1.342
found = False

print(name)
print(age)
print(price)
print(found)


# conditionals
if( age < 99 ):
    print("Don't worry, you are still young!")
    print("Same indentation")
    print("inside if")

elif( age == 99):
    print("You are on the border line")

else:
    print("Sorry you are old")


print("outside if")



# functions 
def test():
    print("Hello from a function")
    print("I'm inside too")

    if 3 < 2:
        print("Of course it is")



def hello():
    print("Hello Jake")

# execute/call the function
test()
hello()



# create a function that prints your name
# call that function with

