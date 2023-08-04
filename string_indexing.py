lang='java'
print(lang[2])
# j=0       or -4
# a=1     or -3       
# v=2      or -2
# a=3    or -1   

# string sclicing =two print more than one word

print(lang[1:3])
print(lang[:])  #give full variable
print(lang[1:]) #give s

# string step argument: it will print word by taking giving step
# syntex =vaaria[start:stop:step]

print(lang[1:3:2])

# print opoosite of the given string

print(lang[3::-1])

# exercise: take input from user his name and print it in reverse order

name=input('enter your name ')
print(name[-1::-1])