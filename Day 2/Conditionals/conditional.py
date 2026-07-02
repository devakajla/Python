"""
color=input("Enter color (green, red, yellow): ")
if color=='green':
    print('Go')
elif color=='red':
    print('Stop')
elif color=='Yellow':
    print('look')
else:
    print('Not a valid color')
"""

# Practice on conditional
age=int(input("Enter your age:"))

if age<13:
    print('Child')
elif age>13 & age<18:
    print('Teenager')
elif age>18:
    print('Adult')
