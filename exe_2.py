# Variable in python
# Variable is use to store all type data structure value like no,sring,speciol char,
# pyton has daynamic progaraming lang mean value of variable changable also it has no requird t specify data type 

no1=2
print(no1)
name='Durgesh'
print(name)

'''some rule for ake Variable name 
1- 1st latter is start with letter or _(under scoer)
  1name=Durgesh    give error 
  name1 =Durgesh    no error
2- we can not use speciol char in vaariable name '''

user_one_name='Rohit'                   #snake case writing (used for Python)
UserOneNmae='Rohit'                     #cammel case writing(used for java)


# Sring : COllection of of character insid single or double quate 

# string concatination : add two string variable in a single

first_name='Durgesh' 
last_name='Singh'
Full_name= first_name+' '+last_name
print(Full_name)
# print(Full_name + 3)
print(Full_name + '3')
print((Full_name +' ') * 3)

# input function is use to take any input by the user
# input function take input in string 
name=input('enter your name ')
print('hello '+ name)

# taking two value from user and sum them also print the result

num1=input('Enter the first no')
num2=input('Enter the second no')
sum=int(num1)+int(num2)
print('Sum of the valuse is '+'sum') 
