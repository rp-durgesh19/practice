def squre(a):
    squre=[]
    for i in a:
        squre.append(i**2)
    return squre 
def cube(a):
    cube=[]
    for i in a:
        cube.append(i**3)
    return cube
lst=[]
while len(lst)<5:
    num=int(input('Enter the no :  '))
    number=lst.append(num)
print(f"Your list is:  {lst}")
print(f"Squre of the list is:  {squre(lst)}")
print(f"Cube of the list is:  {cube(lst)}")


