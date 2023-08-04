# print hello world 10 times

# for i in range(10):
#     # print("hello world")



# for i in range(1,11):
    # print(f"hii {i}")



# sum of n natural no


# no=int(input("Enter your last no"))
# sum=0
# for i in range(1,no+1):
#     sum+=i
#     print(f'{sum-i} + {i} = {sum}')


# input <2digit and sum it

# no=input("Enter your no ")
# sum=0
# if int(no) > 10:
#     for i in range(0,len(no)):
#         sum+=int(no[i])
#     print(int(sum))



# input user name and print the char index 

# name=input('Enter your name : ')
# for i in range(len(name)):
#     print(f'{name[i]} : {i}')

# input user name and print the how many times that char in string

name=input('Enter your name : ')
temp=''
for i in range(len(name)):
    if name[i] not in temp:
        print(f'{name[i]} : {name.count(name[i])}')
        temp+=name[i]