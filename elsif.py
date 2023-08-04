# elseif is used to check more than on condition

age=int(input('Enter you age'))
if age <= 3:
    print('ticket price = Free')
elif 3< age <= 18:
    print('ticket price = 100')
elif 18< age <=60:
    print('ticket price = 200')
else:
    print('ticket price = 250')