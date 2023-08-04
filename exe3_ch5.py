def rev(l):
    rever=[]
    for char in l :
        rever.append(char[::-1])
    return rever
name=['durgesh','singh']
print(rev(name))