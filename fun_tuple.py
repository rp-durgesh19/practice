# when we can return more than two values it return in tuple 

def fun(num1,num2):
    add=num1+num2
    mul=num1*num2
    divide=num1/num2
    return add , mul , divide

print(fun(4,5))