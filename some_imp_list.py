# generate list with range method

number=list(range(1,21))
# print(number)

# # more about pop method
# item=number.pop()
# print(item)
# print(number)


# # index method
# # find place of any item
# print(number.index(8,0,21))     # here we cangive where seaching start

# # pass list to a function

def nega_list(a):
    num=[]
    for i in a:
        num.append(-i)
    return num

print(nega_list(number))
