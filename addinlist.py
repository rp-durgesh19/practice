fruit=['mango','banana']
fruit.append('grapes')               #it was add data in last of the list and it was add only one data 
print(fruit)


fruit.insert(1, 'grapes')
print(fruit)


fruit1=['mango','apple']
fruit2=['banana','orange']
frui=fruit1+fruit2                  #add two list and store a new list
print(frui)

fruit1.extend(fruit2)              #it was add data in last of the list as new element of the list 
print(fruit1)                   
fruit1.append(fruit2)               #it was add data in last of the list as list in list 
print(fruit1)