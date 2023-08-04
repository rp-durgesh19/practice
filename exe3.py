# make gaussing no game

win_no='4'
user=input('Enter any no between 1 to 10 :')
if user==win_no:
    print('You Win')
else:
    if user >  win_no:
        print('You are too high')
    else:
        print('You are too low')