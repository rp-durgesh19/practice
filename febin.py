def feb(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        print(f'{a},{b}',end=",")
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            print(c ,end=',')

no=input('Enter no of febinacci serise : ')
print('Serise is = ' ,end ='')
a=feb(int(no))