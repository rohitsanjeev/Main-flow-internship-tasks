# Creating a list
my_list = [10, 20, 30, 40, 50]

# Adding an element to the list
my_list.append(60)

# Removing an element from the list
my_list.remove(30)

# Modifying an element in the list
my_list[0] = 100
print('Updated  list:', my_list)

# Creating a dictionary
my_dict = {'name': 'ram', 'age': 22, 'city': 'hyd'}

# Adding 
my_dict['gender'] = 'Male'

# Modifying 
my_dict['age'] = 21

# Removing 
del my_dict['city']
print("Updated Dictionary:", my_dict)

# Creating a set
my_set = {10, 20, 30, 40}

# Adding elements
my_set.add(50)

# Modifying (adding multiple elements)
my_set.update({70, 80})

# Removing elements
my_set.remove(30)

print("Updated Set:", my_set)