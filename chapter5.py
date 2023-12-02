#slicing lists
players=['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])

#slicing lists in a for loop
print("here are the first 3 players on the team:")
for player in players[:3]:
    print(player.title())

#copying and editing lists
my_foods = ['pizza', 'tacos', 'cake']
friend_foods = my_foods[:]
print("my fav foods are")
print(my_foods)
print("\nMy friend's fave foods are")
print(friend_foods)
my_foods.append('lefse')
friend_foods.append('ice cream')
print("my fav foods are")
print(my_foods)
print("\nMy friend's fave foods are")
print(friend_foods)

#tuples - lists you cannot change - regular ()
dimensions= (200,50)
print('OG dimensions')
for dim in dimensions:
    print(dim)

# dimensions[0]=25 <-- ILLEGAL
dimensions = (400,100)
print('New dimensions')
for dim in dimensions:
    print(dim)


#if statements
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())

if "audi" in cars:
    print("There is an audi")

age0=22
age1=18
if age0>=21 and age1>=21:
    print("Yes")
else:
    print("NO")

if age0>=21 or age1>=21:
    print("Yes")
else:
    print("NO")

toppings = ['mushroom', 'onion', 'pineapple']

if 'mushroom' in toppings:
    print("yes mushrooms!")
else:
    print("no mushrooms")

if 'sausage' in toppings:
    print("yes sausage!")
else:
    print("no sausage")
    
if 'peppers' not in toppings:
    print('do you also want peppers?')

