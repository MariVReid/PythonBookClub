# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 19:40:20 2023

@author: mariv
"""

print("Hello python world")

message = "hello python world"
print(message)

message = "hellow python crash course world"
print(message)

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name= "ada"
last_name="Lovelace"
full_name= f"{first_name} {last_name}"
print(full_name)
message = f"hello, {full_name.title()}!"
print(message)

favorite_language='python '
favorite_language
favorite_language.rstrip()
favorite_language
favorite_language = favorite_language.rstrip()
favorite_language


nostarch_url = 'https://nostarch.com'
nostarch_url.removeprefix('https://')


message = "one of python's strengths is its diverse community"
print(message)


universe_age = 14_000_000_000 #not a super common practice, use scientific notation
print(universe_age)


x,y,z=0,0,0
print(x, y, z)

num = 3**2 #exponent expression, the ^ character is a logical operator

#this is a comment
# in general use "" to define a string, so ' can be used inside the string. Only use '' to define a string if " is used inside the string
# name variables like this - Variable_Name (pascal snake case)
# name constants like this - CONSTANT_NAME (screaming snake case)
# VS code (microscoft) is a programmers go to python writing software
