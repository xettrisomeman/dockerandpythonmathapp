#A simple math app with docker

#creating a class called Math
class Math:

    #initializing a argument
    def __init__(self,argument):
        self.argument = argument

    #do_math function for calculation
    def do_math(self,first_number,last_number):
        if self.argument.lower() in 'addition':
            return first_number+last_number
        elif self.argument.lower() in 'subtract':
            return first_number - last_number
        elif self.argument.lower() in 'multiply':
            return first_number * last_number
        elif self.argument.lower() in 'divide':
            return first_number / last_number
        else:
            return "Sorry , command is out of reach"

#taking argument as use input 
argument = input("What you want to do?")
#first number as user input
first_number = int(input("Type first number"))
#second_number as user input
second_number = int(input("Type second number"))

#creating a object
math = Math(argument)

#printing out the result
print(math.do_math(first_number , second_number))

