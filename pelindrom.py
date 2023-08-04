def peli(n):
    sum=''
    for i in range(-1,-(len(n)+1),-1):
        sum+=n[i]
    if sum==n:
        return True
    return False



name=input('Enter a no or string o check pelindrom or not : ')
print(peli(name))
