#A simple math app with docker

#creating a class called Math
class Math:

    #initializing a argument
    def __init__(self,argument):
        self.argument = argument
        self.first_number = 0
        self.last_number = 0
        self.datas = [
            'addition',
            'add',
            'subtract',
            'sub',
            'subtraction',
            'multiply',
            'multiplication',
            'divide',
            'division',
        ]

    def run_function(self):
        if self.argument in self.datas:
            #first number as user input
            self.first_number = int(input("Type first number "))
            #second_number as user input
            self.last_number = int(input("Type second number  "))
            self.do_math()
        else:
            return "Sorry , command is out of reach"

    #do_math function for calculation
    def do_math(self):
        if self.argument.lower() == 'addition' or self.argument.lower() == 'add':
            return f"The addition value is {self.first_number+self.last_number}"
        elif self.argument.lower() == 'subtract' or self.argument.lower() == 'sub' or self.argument.lower() == 'subtraction':
            return f"The subtraction value is {self.first_number-self.last_number}"
        elif self.argument.lower() == 'multiply' or self.argument.lower() == 'multiplication':
            return f"The multiplication value is {self.first_number*self.last_number}"
        elif self.argument.lower() == 'divide' or self.argument.lower() == 'division':
            return f"The division value is {self.first_number/self.last_number}"




#taking argument as use input 
argument = input("What you want to do? ")


#creating a object and passing arugment
math = Math(argument)

#printing out the result
print(math.run_function())

