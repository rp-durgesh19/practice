def name(first,last,age):
    print(f'Your name is {first} {last} and your age is {age}')

name('durgesh','singh',19)            # no error
# name(durgesh, singh)            # give error normal when def name(first,last,age=19): or def name(first,last,age=none): give no error 
                                    #that was make as default parameter 
# name(durgesh, 19)            # give error you can't make default parameter in mid you can make default parameter from right to left 