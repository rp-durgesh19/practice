 # while loop:?

i=1
# while i<=10:
#     print(f'hello Durgesh{i}')
#     i+=1
# sum=0
# while i<=10:
#     print(f'{i}+\b ')
#     sum+=i
#     i+=1
# print(sum)


# Exercise 1
# 1=sum of n natural no 
# 2=ask user for natural no
# 3=print total from 1to n

# i,sum=1,0
# no=int(input('Enter the last no : '))
# while i<=no:
#     sum+=i
#     i+=1
# print(f'sum of the {no} natural no is {sum}')


# execise 2
# take input from user and sum of the digit which is enter by the user

# sum=0
# no=int(input("enter the no more than 1 digit : "))
# if no>=10:
#     while no>0:
#         n=int(no%10)
#         no/=10
#         sum+=n
#     print(sum)
# else:
#     print('please enter more than 2digit no ')


# Exercise 3
# take user name and print count of each word 

n=0
name=input('Enter your name : ')
i=len(name)
while n<i:
    c=name.count(name[n])
    print(f"{name[n]} = {c}")
    n+=1
