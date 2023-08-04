def com(l,m):
    comm=[]
    for i in l:
        for j in m:
            if i==j:
                comm.append(i)
    return comm

num1=[1,2,3,4,5]
num2=[1,3,4,6,7,8]
print(com(num1, num2))
