UserName = input('Creat a User Name: ')

EmailAddress = input('Enter a valid email address: ')

ValidEmailAddress = input('Confirm your email address: ')


for name in UserName:

    if ValidEmailAddress == EmailAddress:

        print('Confirmed')

else:

        print('Please enter a valid email address')

# Unable to insert a break without it crashing. Runs fine without. 

        break

print('Your User Name is :', UserName)
