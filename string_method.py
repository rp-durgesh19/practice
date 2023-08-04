# some imp func in string
name='Durgesh Singh'

# len() function: use to count char in string

print(len(name))
length=len(name)
#  lower() method: use to print all string in smal latter

print(name.lower())

#  upper() method : use to make all string in uppercase 

print(name.upper())

#  title() method: after space first char it will make uppercase 

print(name.title())

#  count() \mathod : use to find a char how many times come in our string 

print(name.count('g'))


# exercise =taking two comma seprated input from the user and one single char which is in our string 

name,char=input('Enter your name '),input('Enter the char')
print(len(name.replace(' ', '')))
print(((name.replace(' ', '')).lower()).count((char.replace(' ', '')).lower())) 



