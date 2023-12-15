message = input("I am a parrot bawk\n") #input always stores response as a string
print(message)
snow_white = input("\nWho is the fairest of them all: ")
print(f"{snow_white} is the fairest of them all")

prompt = "\nWhat is your first name?"
prompt += "\nOh and what is your last name? "
name = input(prompt)
print(f"Hi {name}")

age = input("\nHow old are you? ")
age=int(age)
if age>= 18:
    print('you are an adult!')
else:
    print('you are a child')
    
number= input("\nGive me a number ")
number=int(number)
if number %2==0: #The % sign gives the remainder of a division
    print('the number is even\n')
else:
    print("the number is odd\n")
    

current_number=1
while current_number <=5:
	print(current_number)
	current_number +=1
 
prompt= "\nBawk I am a parrot bawk (Say STOP to shut me up) "
message=""
while message != "STOP":
	message=input(prompt)
	print(message)
 
prompt= "\nBawk I am BETTER a parrot bawk (Say STOP to shut me up) "
message=""
active=True
while active: #this is using a flag
    message=input(prompt)
    if message == 'STOP':
        active = False
    else:
        print(message)

prompt = "\nPlease enter the name of a state (Say STOP if done) "
while True:
    city= input(prompt)
    if city== 'STOP':
        break
    else:
        print(f"{city.title()} is a nice place to visit")
        
number = 0 
while number<10:
    number+=1
    if current_number% 2==0:
        continue
    print(current_number)
    
# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print(f"Verifying user: {current_user.title()}")
	confirmed_users.append(current_user)
#Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
print(confirmed_user.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
	pets.remove('cat')
print(pets)