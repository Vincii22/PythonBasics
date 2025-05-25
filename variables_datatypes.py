name = 'Arvin'
password = 'redblood12'

names = input('Enter Username: ')
passwords = input('Enter Password: ')

if names == name and passwords == password:
    print('Hello Arvin')
elif names != name and passwords != password:
    print('Incorrect Credentials')
elif names != name:
    print('Incorrect UsernameJa')
elif passwords != password:
    print('Incorrect Password')
