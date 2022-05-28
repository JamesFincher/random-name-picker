import random

#Get names from user
name_string = input("Please supply names, each separated by commas... For example \n Tom, Jason, Carl, Sarah \n \n Names:")

#Convert names to an easy to access list
parsed_names = name_string.split(", ")

#Select and set a random name from the list
random_name = random.choice(parsed_names)

#Return the random name to the user
print(f"\n The random name selected is {random_name}")