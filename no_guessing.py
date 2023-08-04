
win=33
for i in range(4):
    no=int(input('Enter any no 0 to 100 : '))
    if no==win:
        print('You win')
        print(f'You have remember {3-i} attampt')
        break
    elif i==3:
        print('You lose')
        print(f'You have remember {3-i} attampt')
        break
    elif no > win:
        print('ohho ! You are too high')
        print(f'You have remember {3-i} attampt')
        continue
    elif no < win:
        print('Ohho ! You are too low')
        print(f'You have remember {3-i} attampt')