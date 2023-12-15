#Chapter 5 part 2 
age = 19
if age>= 18:
    print("You can vote")
else:
    print("you are to young to vote, try again next year")

age = 16
if age>= 18:
    print("You can vote")
else:
    print("you are to young to vote, try again next year")

age = 12
if age<4:
    print("your admission is free")
elif age<18:
    print('your admission cost is $20')
elif age>60:
    print('your admission cost is $25')
else:
    print("Your admission cost is $40")
    
toppings=['sausage', 'green pepper', 'extra cheese']
for topping in toppings:
    if topping == 'green pepper':
        print('No peppers for you')
    else:
        print(f"Adding {topping}")
print('pizza is here!')

topping_list = []
if topping_list:
    for topping in toppings:
        print(f"Adding {topping}")
else:
    print("Just cheese pizza... okay")
print('pizza is here!')

possible_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'ham', 'pineapple']
request = ['ham', 'pineapple', 'onion']

for topping in request:
    if topping in possible_toppings:
        print(f"Adding {topping}")
    else:
        print(f"we don't have {topping}")
print('pizza is here!')


#Chapter 6
alien_0 = {} #creating an empty dicitonary that you can fill
alien_0 = {'color':'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)
del alien_0['points']
print(alien_0)
point_value =alien_0.get('points', 'no points assigned')
color_value = alien_0.get('color', 'no color assigned')
print(point_value)
print(color_value)

research = {
    'mari':'the nucleus',
    'phil':'muscle',
    'bob':'protein stucture',
    'crystal':'aging'
}
for person, topic in research.items():
    print(f"\n{person.title()} likes to study {topic}.")
print("\n")

for person in research.keys(): #you don't really need .keys()
    print(person.title())

for name in sorted(research.keys()):
    print(f"\n{name.title()} is in python book club.")

print("\nBook club is intrested in:")
for topic in research.values():
    print(topic.title())

program = {
    'mari':'mcdb&g',
    'phil':'bmbb',
    'crystal' : 'bmbb',
    'bob':'faculty'
}

print("\nBook club is from:")
for P in set(program.values()):
    print(P.upper())
    
# Creating a set (will auto correect to remove duplicates):
# breed = {'beagle', 'collie', 'poodle', 'poodle'}

alien_0= {'color':'green', 'points':5}
alien_1 = {'color':'yellow', 'points':10}
alien_2 = {'color':'red', 'points':15}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
    
#for alien_number in range (30):
    #new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    #aliens.append(new_alien)

#pizza = {
    #'crust':'thick',
    #'toppings': ['pineapple', 'ham']
#}
#for topping in pizza['toppings']:
    #print(f"\t{topping}")
    

#input("Press <enter> to continue") 
# ^This (without asignment) allows you to run in chunks

#User imput of a dictionary
user_info={}
while(True):
    user_input_name = input("Username (or enter to exit) ")
    if user_input_name == "":
        break
    user_input_password = input("password ")
    user_info[user_input_name]= user_input_password
    
    

    