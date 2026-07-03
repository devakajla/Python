username=input('Enter the username: ')
password=input('Enter the password: ')

# if (username=='admin' and password=='pass'):
#     print('User is valid')
# else:
#     print('User is not valid')
    

if (username=='admin' and password=='pass'):
    print('LOGIN Successful')
else:
    if username!='admin':
        print('Wrong Username')
    elif password!='pass':
        print('Wrong Password')