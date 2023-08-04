def fil(l):
    ls=[]
    odd=[]
    even=[]
    for i in range(len(l)):
        if l[i]%2==0:
            even.append(l[i])
        else:
            odd.append(l[i])
    ls.append(odd)
    ls.append(even)
    return ls

num=[1,2,3,4,5,6,7,8,9,10,11]
print(fil(num))