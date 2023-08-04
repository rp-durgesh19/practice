# def rever(a):
#     rever=[]
#     rever.append(a[::-1])
#     return rever

def rever(a):
    rever=[]
    for i in range(len(a)):
        rever.append(a.pop())
    return rever



num=[1,2,3,4,5,6]
# print(rever(num))
num.reverse()
print(num)

num.remove(2)
print(num)