# In nesting we have conditionals inside conditions

# if
#   if
#   else

username=input('Enter the username: ')
password=input('Enter the password: ')
   

if (username=='admin' and password=='pass'):
    print('LOGIN Successful')
else:
    if username!='admin':
        print('Wrong Username')
    elif password!='pass':
        print('Wrong Password')