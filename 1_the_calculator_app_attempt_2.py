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

operation_choice = input("What operation do you want to perform? (addition, subtraction, multiplication, division): ")
parameter_list = []
if operation_choice == "addition":    
    while True:
        try: 
            add_terms = input("What terms would you like to add? (when finished type done): ")
            if add_terms == "done":
                break
            parameter_list.append(float(add_terms))
        except:
            print("Terms have to be numbers")
            continue
    print(addition(*parameter_list))
if operation_choice == "subtraction":
    start_sub = input("What is the first term you would like to subtract from?: ")
    while True:
        try:
            sub_terms = input("You would like to subtract by (when finished type done): ")
            if sub_terms == "done":
                break
            parameter_list.append(float(sub_terms)) 
        except:
            print("Terms have to be numbers")
            continue
    print(subtraction(float(start_sub), *parameter_list)) 
if operation_choice == "multiplication":
    while True:
        try:
            multiply_terms = input("What terms would you like to multiply? (when finished type done): ")
            if multiply_terms == "done":
                break
            parameter_list.append(float(multiply_terms))
        except:
            print("Terms have to be numbers")
            continue
    print(multiplication(*parameter_list))
if operation_choice == "division":
    start_divide = input("What number would you like to divide from?: ")
    while True:
        try:
            divide_terms = input("What numbers would you like to divide by? (when finished type done): ")
            if divide_terms == "0":
                print("You cannot divide by zero, please enter a different divisor")
                continue
            if divide_terms == "done":
                break
            parameter_list.append(float(divide_terms))
        except:
            print("Terms have to be numbers")
            continue
    print(division(float(start_divide), *parameter_list))

'''
Contains Tasks 1-3. Second attempt after first attempt tried to take user inputs in 
its own functions. When doing that attempt I was unable to solve how to account for 
zero division error, and realized I could only do so if I separated division from 
subtraction making those last two functions more harmful than helpful. You cannot test if 
a certain argument is being made in a function with an if loop! Thus this term breaks up 
those two functions from attempt 1 into more if tests and the four while loops have nested 
try/except terms to catch any errant user entries such as string where a number is 
expected.
'''