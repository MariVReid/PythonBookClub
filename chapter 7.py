### Bob's Problem to Fix
### Dictionary in a dictionary...
# dictionaries defined...              NOTE: Be careful of the commas!
users = {
	'aeinstein':
		{
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},
	'mcurie':
		{
		'first': 'marie',
		'last': 'cury',
		'location': 'paris',
		},
	'pwoods':
		{
		'first': 'phil',
		'last': 'woods',
		'location': 'UMN',
		},
} 	

# print it all out...
for username in users.items():               # the top level...
	print(f"{username}")

		
print("\n-----\n")


for username, users in users.items():        # another level...
	print(f"{users['last']}")


test_name = "bob"
print(f"\n----- {test_name.title()} -----\n")  # making sure this works...


#for username, users in users.items():        # capitalize...  What!!!??  Why??
#	print(f"{users['last'].title()}")
#

print("\n-----\n")


for username, users in users.items():        # Another way... Argh! What's wrong here!
	lastname = (users['last'])
	firstname = (users['first'])
	print(f"One of the scientists: {firstname.title()} {lastname.title()}")