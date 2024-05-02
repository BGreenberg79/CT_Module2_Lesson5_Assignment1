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

choose_operation = input("What operation would you like to use (addition, subtraction, multiplication, division): " )
if choose_operation == "addition":
    addition_list = []
    while True:
        add_terms_input = input("What numbers would you like to total? (If finished type 'done'): ")
        if add_terms_input != 'done':
            addition_list.append(int(add_terms_input))
        if add_terms_input == 'done':
            break
    user_output_add = addition(*addition_list)
print(user_output_add)
#Tutor Daniel said to try subtract, multiplication, division by calling function
def chose_subtract():
    while True:
        sub_terms_input = input("What numbers would you like to subtract? (If finished type 'done'): ") #how do I change this for start parameter "x" before the subtraction list *args?
        if sub_terms_input != "done":
            subtraction_list.append(int(sub_terms_input))
        if sub_terms_input == "done":
            break

if choose_operation == "subtraction":
    subtraction_list = []
    chose_subtract()
    user_output_subtract = subtraction(, *subtraction_list)
print(user_output_subtract)