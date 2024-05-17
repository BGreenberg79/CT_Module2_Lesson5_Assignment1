# Task 1 Write a function that lets users add items to list

def add_item():
    global shopping_list 
    shopping_list = []
    while True:
        added_item = input("What item would you like to add to the shopping list (when finished type 'done'): ")
        if added_item == "done":
            break
        shopping_list.append(added_item)

add_item()

# Task 2 include a feature to remove items from the list

def remove_item():
    global shopping_list
    while True:
        try:
            removed_item = input("What item would you like to remove from the list (when finished type 'done'): ")
            if removed_item == "done":
                break
            shopping_list.remove(removed_item)
        except:
            print("User input is not an item from the shopping list")
            continue

remove_item()

# Task 3 Add function that prints out list in formatted way

def print_list():
    global shopping_list
    shopping_list = [titled_item.title() for titled_item in shopping_list]
    print("The shopping list includes the following items: ")
    print(*shopping_list, sep = "\n")

print_list()