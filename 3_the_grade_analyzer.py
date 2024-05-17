# Task 1 Code a function to calculate the Grade Point average

def mean_grades(*student_grades):
    return sum(student_grades) / len(student_grades)

grade_list = []
while True:
    try:
        enter_grades = input("Please enter all student grades (when finished type 'done'): ")
        if enter_grades == "done":
            break
        grade_list.append(float(enter_grades))
    except:
        print("Please enter a valid numbered grade")
        continue
print("The mean grades computes to:", mean_grades(*grade_list))

# Task 2 Implement a function to find the highest and lowest grades

def highest_grade():
    grade_list.sort()
    print("The highest grade is:", grade_list[-1])

highest_grade()

def lowest_grade():
    grade_list.sort(reverse=True)
    print("The lowest grade is:", grade_list[-1])

lowest_grade()

# Task 3 Categorize grades into letters

for grade in grade_list:
    if grade >= 90:
        print(f"{grade} is an A grade")
    elif grade >= 80:
        print(f"{grade} is a B grade")
    elif grade >= 70:
        print(f"{grade} is a C grade")
    elif grade >= 60:
        print(f"{grade} is a D grade")
    else:
        print(f"{grade} is a F grade")