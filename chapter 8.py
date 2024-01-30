#Chapter 8
def greet_user(username):
    """Displays a simple greeting"""
    print(f"\nHello, {username.title()}!")

greet_user('python book club')

def display_angry_message(mess):
    print(f"\n{mess.upper()}")
    
display_angry_message('i am yelling at you')

def describe_animals(type, name):
    print(f"\nI have a pet {type} its name is {name.title()}.")

describe_animals('rabbit', 'gizmo')
describe_animals('dog', "bella")

def describe_animals2(animal_type, pet_name='bubbles'): #The ones without defaults must go first, and stay in order
    print(f"\nI have a pet {animal_type} its name is {pet_name.title()}.")

describe_animals2(pet_name='gizmo', animal_type='bunny')
describe_animals2(animal_type='fish')

def make_shirt(message, size='M'):
    print(f"\nYour shirt will be size {size} and say '{message}' on it")

make_shirt("Bob's Book Club")

def format_name(first, last, middle=''):
    if middle:
        full_name= f"{first} {middle} {last}"
    else:
        full_name= f"{first} {last}"
    return full_name.title()

K = format_name("Agatha", "Christie")
print(K)
K = format_name("Mari", "Reid", "Vevle")
print(K)

def build_monster(head, body, tail, wing=""):
    monster={'head':head, 'body':body, 'tail':tail}
    if wing:
        monster['wing']=wing
    return monster
monster=build_monster('lion', 'armidillo', 'rattle snake', 'parrot')
print(monster)

while True:
    print("\n What do you want your monster to look like?")
    print("Type 'x' to quit")
    h=input("Head: ")
    if h=='x':
        break 
    b=input("Body: ")
    if b=='x':
        break 
    t=input("Tail: ")
    if t=='x':
        break 
    m= build_monster(h, b, t)
    print("Your monster will have these features:")
    print(m)


def hi_BC(names):
    print(f'\n')
    for name in names:
        m=f"Hi {name.title()}"
        print(m)
names=['phil', 'bob', 'mari' , 'crystal']
hi_BC(names)
#send a copy of a list like this function(list_name[:]). This way it won't permenently modify the original

def pizza(*toppings): #arbitrary arguments must come last, two * (**) creates a dictionary containing name/value pairs passed in
    print('\nyour pizza has:')
    for t in toppings:
        print(f"-{t}")
pizza("cheese")
pizza("olives", "anchovies", "pineapple")