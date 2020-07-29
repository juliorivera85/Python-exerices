## Exercises

################
### CH 3 #######
################

#3-1
f_names = ["mac", "kelvin", "ben", "hailey", "edmund"]
print(f_names[0].title()) #first name on list
print(f_names[1].title()) #second name on list
print(f_names[2].title()) #third name on list
print(f_names[-1].title()) #last name on list

#3-2
message = "I hope you, " + f_names[0].title() + ", are doing well."
print(message)
message1 = "I hope you, " + f_names[1].title() + ", are doing well."
print(message1)

#3-3
cars = ["BMW", "Jeep", "VW", "Honda"]
message = "I would like to own a " + cars[0].upper() + " someday!"
print(message)
message1 = "I would like to own a " + cars[-1].lower() + " someday!"
print(message1)

## Exercies
#3-4
dinner = ["jesus", "jo", "amy"]
print(dinner)

#3-5
print(dinner[0])
dinner[0] = "grant"
message = "I can't wait for you, " + dinner[0] + " to stop by"
print(message)
message1 = "I can't wait for you, " + dinner[1] + " to stop by"
print(message1)

#3-6
print(dinner)
dinner.insert(0, "wash")
dinner.insert(2, "morgan")
dinner.append("marge")
print(dinner)


#3-7
print(dinner)
message = "I can only invite two people for dinner"
print(message)

#remove last guest in list and write them a message
guest1 = dinner.pop()
message = "I'm sorry " + guest1 + " but I can't have you over."
print(message)
guest2 = dinner.pop()
message = "I'm sorry " + guest2 + " but I can't have you over."
print(message)
guest3 = dinner.pop()
message = "I'm sorry " + guest3 + " but I can't have you over."
print(message)
guest4 = dinner.pop()
message = "I'm sorry " + guest4 + " but I can't have you over."
print(message)

#delete last 2 names to have an empty list
print(dinner)
del dinner[0]
del dinner[0]
print(dinner)

##Exercises
#3-8
places = ["uk", "egypt", "antartica", "sa", "germany"]
print(places)

#temp sort
print(sorted(places))
print(places)

places.reverse()
print(places)
places.reverse()
print(places)


# permanently change list to alphabetical order
places.sort()
print(places)

#reverse alphabetical 
places.sort(reverse=True)
print(places)

#3-9
dinner = ["jesus", "jo", "amy"]
message = "I will be having " + str(len(dinner)) + " over for dinner."
print(message)


#################
## CH 4 #########
################


##Exercise chapter 4
#4-1
pizzas = ["cheese", "pep", "chicken"]
for pizza in pizzas:
	message = "\nI like " + pizza + " pizza!"
	print(message)
print("I really love all pizzas!")

#4-2
animals = ["cat", "dog", "bear"]
for animal in animals:
	message = "\nA " + animal + " would make a great pet"
	print(message)
print("\nAny of these animals would make great pets")

## Exercises
#4-3
numbs = [value for value in range(1,21)]
print(numbs)
#OR
numbs = []
for value in range(1,21):
	numbs.append(value)
print(numbs)

#4-4
mil = [value for value in range(1, 1000001)]
print(mil)

#4-5
min(mil)
max(mil)
sum(mil)

#4-6
odd_numbers= [value for value in range(1,21,2)]
print(odd_numbers)

#4-7
threes = [value for value in range(3,31, 3)]
print(threes)


#4-8
cubes = []
for value in range(1,11):
	cubes.append(value**3)
print(cubes)

#4-9
cubes = [value**3 for value in range(1,11)]
print(cubes)


##Exercises
#4-10
my_foods.append("jelly")
my_foods.append("choc")
my_foods.append("water")
print(my_foods)

print("The first three items on the list are:")
print(my_foods[0:3])

print("Three items from the middle of the list are:")
print(my_foods[2:5])

print("The last three items on my list are:")
print(my_foods[-3:])

#4-11
pizzas = ["cheese", "pep", "chicken"]
friends_pizza = pizzas[:]
print(friends_pizza)

friends_pizza.append("mush")
print(friends_pizza)

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("My friends favorite pizzas are:")
for pizza in friends_pizza:
	print(pizza)

#4-12
#first method
pizzas = ["pepo", "garlic", "chix", "cheese"]
my_pie = []
for piz in pizzas:
	my_pie.append(piz)
print(my_pie)

#second method
my_pie2 = [print(piz) for piz in pizzas[:]]


#Exercise
#4-13
foods = ("chx", "beef", "fish", "crab", "shrimp")
print(foods)
#foods[0] = "turkey"

foods = ("chx", "beef", "fish", "lettuce", "cheese")
for food in foods:
    print(food)

#######################
## CH 5 ###############
#######################
#Exercises
#5-1
car = "subaru"
print("Is car == 'subaru'? I predicts True")
print(car == "subaru")
print(car == "bmw")

#5-2
#test of equality and inequality
topping = "mushroom"

if topping == "mushroom":
    print("Add shrooms")


if topping != "carrots":
    print("hold the carrots")

# test using the lower function    

names = ["MARK", "HEATHER", "JEN", "JOHN"]
name = "MARK"

if name in names:
    print(name.lower())


#execises
#5-3

alien_color = "green"

if alien_color == "green":
    print("You have earned 5 points")

#5-4 if and if/else chains
alien_color = "red"

if alien_color == "green":
    print("You have earned 5 points!")
if alien_color != "green":
    print("You have earned 10 points")


if alien_color == "green":
    print("You have earned 5 points!!!")
else:
    print("You have earned 15 points!!!")


#5-5 elif chains
alien_color = "red"

if alien_color == "green":
    print("You have earned 5 points@!")
elif alien_color == "yellow":
    print("You have earned 10 points@!")
else: 
    print("You have earned 15 points @!")

alien_color = "red"

if alien_color == "yellow":
    print("You have earned 5 points@!")
elif alien_color == "yellow":
    print("You have earned 10 points@!")
else: 
    print("You have earned 15 points @!")

alien_color = "green"

if alien_color == "green":
    print("You have earned 5 points@!")
elif alien_color == "yellow":
    print("You have earned 10 points@!")
else: 
    print("You have earned 15 points @!")
    
## 5-6
age = 77

if age < 2:
    print("this human is a baby")
elif age <4:
    print("this human is a toddler")
elif age <13:
    print("this human is a kid")
elif age <20:
    print("this human is a teenager")
elif age >= 20 and age <=65:
    print("this human is an adult")
elif age > 65:
    print("this human is an elder")

#5-7
favorite_fruits = ["orange", "banana", "grape"]

fruit = "banana"
fruit1 = "watermelon"
fruit2 = "orange"
fruit3 = "pineapple"
fruit4 = "grape"
if fruit in favorite_fruits:
    print("You must really like " + fruit + "!")
if fruit1 in favorite_fruits:
    print("You must really like " + fruit1 + "!")
if fruit2 in favorite_fruits:
    print("You must really like " + fruit2 + "!")
if fruit3 in favorite_fruits:
    print("You must really like " + fruit3 + "!")
if fruit4 in favorite_fruits:
    print("You must really like " + fruit4 + "!")

#5-8
users = ["kel", "jen", "admin", "bob", "roy"]

for user in users:
    if user == "admin":
        print("Hello admin, woud you like to see a status report?")
    else:
        print("Hello " + user + ", thank you for logging in again")



#5-9
users = []

if users:
    for user in users:
        print("Thank you for logging in, " + user + ".")
else: 
        print("we need to find users")
#

#5-10

current_users = ["john", "mary", "paul", "joe", "viv"]
new_users = ["JOHN", "mary", "jane", "bob", "kimo"]

for user in new_users:
    if user.lower() in current_users:
        print("\nYou will have to enter a new name")
    if user.lower() not in current_users:
        print("Ther user name " + user + " is available.")
#
numbs = [1,2,3,4,5,6,7,8,9]

for num in numbs:
    if num == 1:
        print(str(num) + "st")
    elif num == 2:
        print(str(num) + "nd")
    elif num == 3:
        print(str(num) + "rd")
    elif num == 4:
        print(str(num) + "th")
    elif num == 5:
        print(str(num) + "th")
    elif num == 6:
        print(str(num) + "th")
    elif num == 7:
        print(str(num) + "th")
    elif num == 8:
        print(str(num) + "th")
    elif num == 9:
        print(str(num) + "th")
#
#######################
#### CH 6 #############
#######################

#6-1
mac_info = {"first_name": "mac", "last_name": "stecko",
    "age": 31, "city": "denver"}
print(mac_info)
print("My friend's full name is " + mac_info["first_name"].title() + 
    " " + mac_info["last_name"].title() + ".")
print("Mac is " + str(mac_info["age"]) + " years old.")
print("Mac lives in " + mac_info["city"].title() + ".")

#6-2
fav_numbers = {"mac": 31, 
    "anna": 23,
    "jeff": 65,
    "jason": 54,
    "justin": 99
    }
print("Mac's favorite number is " + str(fav_numbers["mac"]) + ".")
print("Anna's favorite number is " + str(fav_numbers["anna"]) + ".")
print("Jeff's favorite number is " + str(fav_numbers["jeff"]) + ".")
print("Jason's favorite number is " + str(fav_numbers["jason"]) + ".")
print("Justin's favorite number is " + str(fav_numbers["justin"]) + ".")

#6-3 make a list of terms and their definitions and print 
# the definition of each one
python_gloss = {"if": "Start of conditional statement",
    "key": "A object that has some value assigned to it",
    "value": "The meaning of key",
    "equality": "determinig if x and y are the same",
    "list": "A series of values stored together",
    }
print("\nAn if is: \n\t" + python_gloss["if"] + ".")
print("A key is: \n\t" + python_gloss["key"] + ".")
print("A value is: \n\t" + python_gloss["value"] + ".")
print("An equality is to: \n\t" + python_gloss["equality"] + ".")
print("A list is: \n\t" + python_gloss["list"] + ".")


#Exercises
#6-4 clean up the following code in a loop:
python_gloss = {"if": "Start of conditional statement",
    "key": "A object that has some value assigned to it",
    "value": "The meaning of key",
    "equality": "determinig if x and y are the same",
    "list": "A series of values stored together",
    }
print("\nAn if is: \n\t" + python_gloss["if"] + ".")
print("A key is: \n\t" + python_gloss["key"] + ".")
print("A value is: \n\t" + python_gloss["value"] + ".")
print("An equality is to: \n\t" + python_gloss["equality"] + ".")
print("A list is: \n\t" + python_gloss["list"] + ".")

#cleaned up code
for key, value in python_gloss.items():
    print("\n A " + key.lower() + " is " + value + ".")

#add 2 more items to the glossary and redo the loop
python_gloss["dictionary"] = "set of key-value pairs"
python_gloss["for"] = "the command to start a forloop"

for key, value in python_gloss.items():
    print("\n A " + key.lower() + " is " + value + ".")
#
#6-5 make a dictionary of rivers and countried
rivers = {"nile": "egypt", "mississippi": "USA", "amazon": "brazil"}

#use a loop to write a sentence
for riv, country in rivers.items():
    print("The " + riv.title() + " runs through " + country + ".")
#
#print out the name of each river

for riv in rivers.keys():
    print(riv.title())

#print out the name of each country
for country in rivers.values():
    print(country)
#
#
#6-6 polling, make a for loop to leave a mesage for people that have 
# taken the poll and people that have not taken the poll

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    }
#
poll = ["ed", "mary", "steven", "jen", "sarah"]

for name in poll:
    if name not in favorite_languages:
        print("Please take our poll, " + name.title() + ".")
    if name in favorite_languages:
        print("Thank you, " + name.title() + " for taking the poll.")
#
## 6-7 people 
people = {
    "mac": {
        "first": "mackenzie",
        "last": "stecko",
        "age": 31,
        "location": "denver",
        },
    "anna": {
        "first": "anna",
        "last": "ciao",
        "age": 37,
        "location": "seattle",
        },
    "ed": {
        "first": "eduardo",
        "last": "muller",
        "age": 35,
        "location": "new jersey",
        },
    }
#
for name, info in people.items():
    print(name.title() + "'s info is: ")
    full_name = info["first"].title() + " " + info["last"].title()
    print("\tFull name: " + full_name)
    print("\tAge: " + str(info["age"]))
    print("\tLives in: " + info["location"].title())

#
## 6-8 pets

pets = { 
    "joey": {
        "kind": "dog",
        "personality": "grumpy",
        "alive": "no",
        "color": "white",
            },
    "tabby": {
        "kind": "cat",
        "personality": "grumpy",
        "alive": "yes",
        "color": "multi",
            },
    "bryan": {
        "kind": "cat",
        "personality": "needy",
        "alive": "yes",
        "color": "black",
            },
        }
#

for name, info in pets.items():
    print("This guy's name is: " + name.title())
    print("\tThey are a " + info["kind"])
    print("\tThey are really " + info["personality"])
    print("\tTheir coat is " + info["color"])
    print("\tAre they alive: " + info["alive"])
#
##6-9
favorite_places = {
    "mac": ["california", "colorado"],
    "kelvin": ["philippines", "hawaii"],
    "spencer": ["california", "mexico"],
    }
for names, places in favorite_places.items():
    print("Hi, I'm " + names.title() + " and here are my fav places: ")
    for place in places:
        print("\t" + place.title())
#
## 6-10
fav_numbers = {"mac": [31, 3254, 75], 
    "anna": [23, 54, 64],
    "jeff": [65],
    "jason": [54, 96, 354],
    "justin": [99, 2143, 0],
    }

for names, numbs in fav_numbers.items():
    if len(numbs) == 1:
        print("I'm " + names.title() + " and my fav number is: ")
        print("\t" + str(numbs))
    else:
        print("I'm " + names.title() + " and my fav numbers are: ")
        print("\t" + str(numbs)) 
#
## 6-11 cities

cities = {
    "paris": {
        "country": "france",
        "population": 8000000,
        "fact": "French is the national language",
            },
    "cairo": {
        "country": "egypt",
        "population": 5000000,
        "fact": "Arabic is the national languange",
            },
    "san salvador": {
        "country": "el salvador",
        "population": 3000000,
        "fact": "Spanish is the national language",
            },
        }
for city, info in cities.items():
    print(city.title() + " is a great city, here is some info: ")
    print("\tIt is located in " + info["country"].title())
    print("\tIt has a population of " + str(info["population"]))
    print("\t" + info["fact"])
#
##6-12

##############################
### CH 7 #####################
##############################

#7-1

car = input("What kind of rental car would you like? ")
print("let me see if I can find a " + car + " for you!")

#7-2
table = input("How many people will be dining with us today? ")
table = int(table)

if table > 8:
    print("you will have to wait for a table for a party of " + str(table) + ".")
else:
    print("Your table is ready!")
#
#7-3

numb = input("Give me a number, any number: ")
numb = int(numb)

if numb % 10 == 0:
    print("The number " + str(numb) + " is a mutltiple of 10")
else:
    print("The number " + str(numb) + " is NOT a multiple of 10") 
##
#7-4
#pizza topiings
prompt = "Please enter your pizza topping: "
prompt += "\n(Enter 'quit' when finished)"


while True:
    topping = input(prompt)
    if topping == "quit":
        break
    else:
        print("Adding " + topping + " to your oder!")
#
## 7-5
#movie tickets

prompt = "How old are you?"


while True:
    age = int(input(prompt))
    if age < 3:
        print("You are " + str(age) + ", so your ticket is free")
    elif age < 12:
        print("You are " + str(age) + ", so your ticket is $10")
    else:
        print("You are " + str(age) + ", so your ticket is $15")

## couldn't get the quit to work the way I want it

##
#7-5
# redo 7-4 and 7-5 with 
# using conditional statements to stop the loop
# use active variabl to control loop
# use break to stop the look 
prompt = "Please enter your pizza topping: "
prompt += "\n(Enter 'quit' when finished)"

active = True

while active:
    topping = input(prompt)
    if topping == "quit":
        break
    else:
        print("Adding " + topping + " to your oder!")
        
####
prompt = "How old are you?"

active = True

while active:
    age = input(prompt)
    if age == "quit":
        break
    elif int(age) < 3:
        print("You are " + str(age) + ", so your ticket is free")
    elif int(age) < 12:
        print("You are " + str(age) + ", so your ticket is $10")
    else:
        print("You are " + str(age) + ", so your ticket is $15")
##
### 7-6 infinity loops

x = "hello, world"

while true:
    print(x)
##
#7-8 deli

sandwich_orders = ["club", "blt", "veggie", "turkey"]
finished_sandwiches = [] 

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich.") 
    
    finished_sandwiches.append(sandwich)
#


print("\nHere is a list of your sanwiches: ")

for sand in finished_sandwiches:
    print("\t" + sand)
    
###
##7-9 no pastrami
#7-9
sandwich_orders = ["club", "pastrami", "blt", "pastrami", "veggie", "pastrami", "turkey"]
print(sandwich_orders)
finished_sandwiches = [] 

print("Sorry, we do not have pastrami today")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich.") 
    
    finished_sandwiches.append(sandwich)

#remove pastrami
while "pastrami" in finished_sandwiches:
    finished_sandwiches.remove("pastrami")


print("\nHere is a list of your sanwiches: ")

for sand in finished_sandwiches:
    print("\t" + sand)
#
##7-10 dream vacation
responses = {}
active_flag = True

while active_flag:
    #prompt the persons response
    name = input("\nWhat is your name? ")
    vaca = input("Where is your dream vacation? ")
    
    #store the responses in a dictionary
    responses[name] = vaca
    
    #find out if anyone else is going to take the poll.
    prompt = input("Would you like someone else to answer (yes/no)? ")
    if prompt == "no":
        active_flag = False

        
#Polling is complete, show the results
print("------ Poll Results -----")
for name, vaca in responses.items():
    print(name.title() + " would like to travel to " + vaca.title() + ".")


######################################
######################################
## Chapter 8 
######################################
######################################

##
#8-1
# message
def display_message():
    """Displays a simple message"""
    print("I'm learning about functions in Ch. 8")

display_message()

##
#8-2
# favorite book
##
def favorite_book(title):
    """Displays favorite book."""
    print("One of my favorite books is " + title.title() + "!")
    
favorite_book("Crime and punishment")

##
#8-3
#T-shirt
def make_shirt(size, text):
    """this makes a shirt"""
    print("You have ordered a " + size + " shirt that says: " + text + ".")

make_shirt("large", "This is my best shirt")
make_shirt(text="This is my other shirt", size="Medium")

##
#8-4
#large shirts

def make_shirt(size="large", text="I love python"):
    """this makes a shirt"""
    print("You have ordered a " + size + " shirt that says: " + text + ".")

#default
make_shirt()

#medium shirt
make_shirt(size="medium")

#different message
make_shirt(text="I love R also")

##
#8-5 cities
#
##
#8-5
#cities

def describe_city(city="reykjavik", country="iceland"):
    """This describes a city and the country it is in"""
    print(city.title() + " is located in " + country.title())
    
describe_city()
describe_city(city="cairo", country="egypt")
describe_city(city="akureyri")
describe_city("vik")

##
#8-6
#Ciry  names

def city_country(city, country):
    info = city + ", " + country
    return info.title()
    print(info.title())
#
FR = city_country("paris", "france")
print(FR)
EG = city_country("cairo", "egypt")
print(EG)
CA = city_country("ottowa", "canada")
print(CA)
    
##
#8-7
#album

def make_album(first_name, last_name, title_name, tracks=""):
    """Makes an dictionary of artists and their albums"""
    if tracks:
        info = {"first": first_name, "last": last_name, "title": title_name, "track": tracks}
    else:
        info = {"first": first_name, "last": last_name, "title": title_name}
    return info

brit = make_album("Britney", "spears", "hit me baby")
print(brit)
beets = make_album("john", "lennon", "yellow")
print(beets)
boys = make_album("fallout", "boys", "under the log")
print(boys)
brit = make_album("Britney", "spears", "hit me baby", 12)
print(brit)

##
#8-8
#user album

def make_album(first_name, last_name, title_name, tracks=""):
    """Makes an dictionary of artists and their albums"""
    if tracks:
        info = {"first": first_name, "last": last_name, "title": title_name, "track": tracks}
    else:
        info = {"first": first_name, "last": last_name, "title": title_name}
    return info
    

while True:
    print("\nLet's get some information about the artist")
    print("(Enter 'q' if you want to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == "q":
        break
    tit = input("Album title: ")
    if tit == "q":
        break
    info = make_album(f_name, l_name, tit)
    print(info)
    
    
##
#8-9
#magicians

magi = ["angel", "blane", "hoodinie"]

def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

show_magicians(magi)

##
#8-10
#great magicians

magi = ["angel", "blane", "hoodinie"]

def make_great(magicians):
    """Adds the great before each name"""
    for magician in magicians:
        print("The Great " + magician.title())

def show_magicians(magicians):
    """Prits a list of magicians"""
    for magician in magicians:
        print(magician.title())

show_magicians(magi)
make_great(magi)

##
#8-11
#unchanged magicians

mags = ["angel", "blane", "hoodinie"]
new_mags = []

def make_great(magicians):
    """Adds the great before each name"""
    while magicians:
        magi = magicians.pop()
        new_mags.append("The Great " + magi)

    

def show_magicians(magicians):
    """Prits a list of magicians"""
    for magician in magicians:
        print(magician.title())

make_great(mags[:])

show_magicians(mags)
show_magicians(new_mags)

##8-12
#sanwiches

def sand_order(*toppings):
    """Prints list of things you want on your sandwich"""
    print("\nHere is what you want on your sandwich: ")
    for topping in toppings:
        print("- " + topping)

sand_order("tomatoes")
sand_order("lettuce", "tomato", "onion")
sand_order("bacon", "turkey", "mayo", "mustard", "lettuce", "onion", "pickles")

##
#8-13
#user profiles
def build_profile(first, last, **user_info):
    profile = {}
    profile["first"] = first
    profile["last"] = last
    
    for key, value in user_info.items():
        profile[key] = value
    
    return profile
jules = build_profile("Julio", "Rivera", hair="red", height="6ft", weight="220")

print(jules)


##
#8-14
#cars
def car_info(maker, model, **car_info):
    """prints information about cars"""
    cars = {}
    cars["maker"] = maker
    cars["model"] = model
    for key, value in car_info.items():
        cars[key] = value
    return cars

car1 = car_info("subaru", "outback", color="blue", tow_package=True) 
print(car1)



##8-15
#printing models
#the module that it is importing has to be in the same directory as the file
# you are wortking on.

import print_models as pm

unprinted_design = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []

pm.print_models(unprinted_design, completed_models)


#8-16
#imports
#importing functions and modules in differen ways

#1
unprinted_design = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []
import print_models
print_models.print_models_new(unprinted_design, completed_models)

#2
unprinted_design = ["coke", "pepsi", "RC-cola"]
completed_models = []
from print_models import print_models_new
print_models_new(unprinted_design, completed_models)

#3
unprinted_design = ["red", "white", "blue"]
completed_models = []
from print_models import print_models_new as pmn
pmn(unprinted_design, completed_models)

#4
unprinted_design = ["cat", "dog", "bird"]
completed_models = []
import print_models as pm
pm.print_models_new(unprinted_design, completed_models)

#5
unprinted_design = ["tree", "bush", "grass"]
completed_models = []
from print_models import *
print_models_new(unprinted_design, completed_models)

##8-17
#styling
#ALWAYS make sure your functions are cleaned and styled correctly


######################################
######################################
## Chapter 9 
######################################
######################################

###9-1
#Restaurant

class Restaurant():
    """info about a restaurant"""
    
    def __init__(self, name, cuisine):
        """Name of restaurant and cuisine type at that restaurant"""
        self.name = name
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        """Describes the type of restaurant"""
        print("The name of the restaurant is " + self.name.title() + ".")
        
    def open_restaurant(self): 
        print(self.name.title() + " is now open.")
        
    def people_served(

restaurant = Restaurant("mcdonalds", "american")

print("The restaurant's name is " + restaurant.name.title() + ".")
print(restaurant.name.title() + " serves " + restaurant.cuisine.title() + " food.")

restaurant.describe_restaurant()
restaurant.open_restaurant()

###9-2
#three restaurants
restaurant1 = Restaurant("panda express", "chinese")
restaurant2 = Restaurant("Qdobo", "mexican")
restaurant3 = Restaurant("basil", "thai")


restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


###9-3
#User


class User(): 
    """Info about users"""
    
    def __init__(self, first_name, last_name, age, login):
        """user information"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login = login
        
    def describe_user(self):
        """Describes user information"""
        print("User's first name is " + self.first_name.title() + ".")
        print("User's last name is " + self.last_name.title() + ".") 
        print("User's age is " + str(self.age) + ".")
        print("User's login name is: " + self.login)
        
    def greet_user(self):
        """Prints a greeting to the user"""
        print("Hello, " + self.login + ", nice to see you again!")
        

user1 = User("james", "palmer", 41, "jpalm")
user2 = User("dani", "hagan", 34, "dhag")
user3 = User("anna", "ciao", 39, "ciaociao")
user4 = User("ed", "muller", 35, "mullermobile")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

user4.describe_user()
user4.greet_user()











