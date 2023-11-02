#creating and indexing lists
bikes = ['trek', 'cannondale', 'redline', 'specialized']
print(bikes)
print(bikes[0])
print(bikes[0].title())
print(bikes[3])
print(bikes[-1])

#using lists in strings
message = f"My first bike was a {bikes[0].title()}"
print(message)

#adding items to lists
motorcycles=['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0]= 'ducati'
print(motorcycles)
motorcycles=['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)
cycles=[]
cycles.append('honda')
cycles.append('yamaha')
cycles.append('kawasaki')
print(cycles)
cycles.insert(0, 'ducati')
print(cycles)

#removing items from lists
motorcycles=['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles)
motorcycles=['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_cycle = motorcycles.pop()
print(motorcycles)
print(popped_cycle)
print(f"The last motorcycle I owned was a {popped_cycle.title()}")
first_own= motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_own.title()}")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
expensive='ducati'
motorcycles.remove(expensive)
print(f"\nA {expensive.title()} is too expensive")

#sort lists
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("here is teh originial list:")
print(cars)
print("\nhere is the sorted list:")
print(sorted(cars))
print("\nI still have the og list")
print(cars)
cars.reverse()
print(cars)

#length of lists
print(len(cars))
