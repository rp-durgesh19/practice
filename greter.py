def greter1(a,b):
    if a>b:
        return a
    return b


# num1=int(input('Enter first no : '))
# num2=int(input('Enter second no : '))

# print(f'Gretest no is {greter(num1,num2)}')



# def greter(no1,no2,no3):
#     if no1>no2 and no1>no3:
#         return no1
#     elif no2>no1 and no2>no3:
#         return no2
#     return no3


# num1=int(input('Enter first no : '))
# num2=int(input('Enter second no : '))
# num3=int(input('Enter third no : '))

# print(f'Gretest no is {greter(num1,num2,num3)}')


# function in function
def greter(no1,no2,no3):
    # big=greter1(no1, no2)
    # return greter1(big, no3)
    # or
    return greter1(greter1(no1, no2), no3)

num1=int(input('Enter first no : '))
num2=int(input('Enter second no : '))
num3=int(input('Enter third no : '))

print(f'Gretest no is {greter(num1,num2,num3)}')