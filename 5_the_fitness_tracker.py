# Task 1 Function to log differet activities and duration
activity_list = []
duration_list = []
# exertion_list = [] this won't work without python dictionaries
def activity_log(activity, duration):
    global activity_list
    global duration_list
    activity_list.append(activity)
    duration_list.append(duration)

activity_log("Basketball", 40)
activity_log("Curling", 120)
activity_log("Football", 60)
activity_log("Weightlifting", 45)
activity_log("Walking", 15)
print("Activities: ", activity_list)
print("Duration:", duration_list)
'''
For this exercise I decided to add to the log I was building by adding to my 
indexed lists by passing arguments into parameters and then appending to my global lists.
This also could work by using an input within a while loop! I was also going to build in an
exertion level parameter which could then run different calorie calculations by activity through an if/elif/else block
but I realied this wouldn't really be possible without dictionaries to associate the items within
each list beyond index.
'''

# Task 2 Calorie burned function

calorie_burned_list = []

def calorie_burned():
    global calorie_burned_list
    global duration_list
    for duration in duration_list:
        calories = duration * 2
        calorie_burned_list.append(calories)

calorie_burned()
print("Calories Burned:", calorie_burned_list)
'''
Here I used a for loop and appended the calories calculated to a global list because return
statements terminate a function and don't work nicely with loops
'''

# Task 3 Create a summary function

def exercise_summary():
    global activity_list
    global duration_list
    global calorie_burned_list
    print("Today's activities included:", ", ".join(activity_list))
    print("Today the total calories burnt were:", str(sum(calorie_burned_list)))

exercise_summary()

'''
I tried to use a nested for loop at one point to try to list how much time was spent doing each
activity but it would not work, much like my earlier attempt to include exertion level. 
I think that level of sophistication in this program would require dictionaries to associate our two lists
That said I used print and the join fuctions to format our activity summary and then turned a sum function
into string to report the calorie total.
'''