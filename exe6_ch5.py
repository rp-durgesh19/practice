def coun(l):
    count=0
    for i in l:
        if type(i)==list:
            count+=1
    return count

num=[1,2,3,[1,2],[5,6],[2,3]]

print(coun(num))