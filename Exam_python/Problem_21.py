# 22. `if-elif-else`

# Fill missing pieces (`____`) of the following code such that prints make sense.

 

name = 'John Doe'

if name:

    print('Name "{}" is more than 20 chars long'.format(name))

    length_description = 'long'

# elif :

#     print('Name "{}" is more than 15 chars long'.format(name))

#     length_description = 'semi long'

# elif ____:

#     print('Name "{}" is more than 10 chars long'.format(name))

#     length_description = 'semi long'

# elif ____:

#     print('Name "{}" is 8, 9 or 10 chars long'.format(name))

#     length_description = 'semi short'

# else:

#     print('Name "{}" is a short name'.format(name))

#     length_description = 'short'

elif 15 < len(name) <= 20:
    
    print('Name "{}" is more than 15 chars long'.format(name))

    length_description = 'semi long'
elif 10 < len(name) <= 15:
    
    print('Name "{}" is more than 10 chars long'.format(name))

    length_description = 'semi long'
elif 8 <= len(name) <= 10:
    
    print('Name "{}" is 8, 9 or 10 chars long'.format(name))

    length_description = 'semi short'
else:

    print('Name "{}" is a short name'.format(name))

    length_description = 'short'

print('The name "{}" is considered a {} name.'.format(name, length_description))
# Expected Output:
# Name "John Doe" is a short name
# The name "John Doe" is considered a short name.
