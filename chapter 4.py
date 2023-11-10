magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thanks y'all/n")

pizzas = ["hawaiian", "uff-dah", "Pep and pepper"]
for pizza in pizzas:
    print(f"{pizza.title()} is one of my fav pizzas!")
print("Katie should get these pizzas for seminar/n")

for value in range (1, 6):
    print(value)
    
numbers=list(range(1,6))
print(numbers)

evens = list(range(2,11,2)) #last number gives step size
print(evens)

squares =[]
for value in range (1,11):
    square = value ** 2
    squares.append(square)
print(squares)

squares2 = [value**2 for value in range(1,11)] #same thing as above but condensed
print(squares2)


for num in range (1,21):
    print(num)

#million = [value for value in range (1, 100000001)]
#print(min(million))
#print(max(million))
#print(sum(million))

odds =[]
for num in range(1, 21, 2):
    odds.append(num)
print(odds)

threes =[]
for num in range(1, 11):
    threes.append(num*3)
print(threes)

cubes = [value**3 for value in range(1,11)] 
print(cubes)
