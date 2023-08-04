
name ="Hii  is durgesh singh from bit. this is located at gkp"
# find:use to find any char string it will give the no of the position where that was located
mn= name.find('is')
print(mn)
print(name.find('is',mn+1))


# replace: tha soud be use to replace old ting with new thing
print(name.replace('is', 'are'))

# example of center method: take users name and print 2# in left and right side of string 

name= input('Enter your name ')
leng=len(name)+4
print((name.strip()).center(leng,'#'))

''' in python string is immutable mean we can not change in our original string python allow 
to change after change it will create a new string it will never change in our original string. '''