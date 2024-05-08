# Task 1 Create functions for each arithmetic function

def addition(*add_terms):
    total = 0
    for number in add_terms:
        total += number
    return total

result_1 = addition(2, 4, 9, 5)
print(result_1)
# Expected output = 20, terminal reports 20
 
def subtraction(x, *sub_terms):
    difference = x
    for sub in sub_terms:
        difference -= sub
    return difference

result_2 = subtraction(100, 50, 10, 5)
print(result_2)
# Expected output = 35, terminal reports 35 

def multiplication(*factor):
    product = 1
    for multiplier in factor:
        product *= multiplier
    return product

result_3 = multiplication(6, 2, 10)
print(result_3)
#Expected output = 120, terminal reports 120 

def division(numerator, *divisor):
    quotient = numerator
    for denominator in divisor:
        quotient /= denominator
    return quotient

result_4 = division(50, 2, 5)
print(result_4)
# Expected output = 5, terminal reports 5 

'''
For each operation I defined a function that would either list the appropriate sum, difference, product, 
or quotient. I knew that to set up these functions in a way where I could string together results
like a simple calculator would,  I needed to use *args parameters and a for loop. As I knew explaining my
work has long been difficult for me in math tests/homework I decided the best way to show my woprk would be
to use a simple test where I would call each function, print the result and compare it to expected results.
I also knew that for subtraction and division the first term of any computation would have to be its own parameter
as you do not start counting from zero or multiplying from onen like you do in those two operations. 
'''

# Task 2  Implement User Input

def calculate_with_one_parameter(operation):
    parameter_list = []
    while True:
        terms_input = input("What numbers would you like to calculate? (If finished type 'done'): ")
        if terms_input != 'done':
            parameter_list.append(float(terms_input))
        if terms_input == 'done':
            break
    return operation(*parameter_list)

def calculate_with_two_parameter(operation):
    start = input("What is the first term you want to calculate from?: ")
    parameter_list = []
    while True:
        terms_input = input("What numbers would you like to calculate? (If finished type 'done'): ")
        # if operation == "division" and int(terms_input) == 0:
        #   print("You cannot divide by zero, please enter a different divisor")
        if terms_input != 'done':
            parameter_list.append(float(terms_input))
        if terms_input == 'done':
            break
    return operation(float(start), *parameter_list)

choose_operation = input("What operation would you like to use (addition, subtraction, multiplication, division): " )
if choose_operation == "addition":
    print(calculate_with_one_parameter(addition))
if choose_operation == "multiplication":
    print(calculate_with_one_parameter(multiplication))
if choose_operation == "subtraction":
    print(calculate_with_two_parameter(subtraction))
if choose_operation == "division":
    print(calculate_with_two_parameter(division))

'''
Built two more functions that took inputs for the list of the numbers to be calculated. One for addition and multiplication as it only required one parameter, 
and another for subtraction and division as those both require a separate start parameter from the listed args parameter that follows.
Those two function conclude by giving a return statement that calls the initial functions from Task 1 once the operation has been identified.
Lastly the if statements correlate to the input that chooses the operation and off of that input then calls the functions we just defined in this task.
'''

#Task 3 Ensure program can handle division by zero and other potential errors

#Because it's set up to just run the function and because subtraction and division are combined I don't know where to put the code for if  terms_input == 0 print ("You cannot divide by zero choose another number")
#Also don't know what other errors could exist. 