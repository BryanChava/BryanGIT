#BRYANCHAVARRIA
#1657040

print('''Davy's auto shop services
Oil change -- $35
Tire rotation -- $19
Car wash -- $7
Car wax -- $12''')

print()


print('Select first service:')
service1 = input()
print('Select second service:')
service2 = input()

print()

print("Davy's auto shop invoice")

print()

total = 0

if service1 == 'Oil change':
    print('Service 1: Oil change, $35')
    total = total + 35

elif service1 == 'Tire rotation':
    print('Service 1: Tire rotation, $19')
    total = total + 19

elif service1 == 'Car wash':
    print('Service 1: Car wash, $7')
    total = total + 7

elif service1 == 'Car wax':
    print('Service 1: Car wax, $12')
    total = total + 12

elif service1 == '-':
    print('Service 1: No service')
    total = total + 0

else:
    print('Service 1: Invalid option')

if service2 == 'Oil change':
    print('Service 2: Oil change, $35')
    total = total + 35

elif service2 == 'Tire rotation':
    print('Service 2: Tire rotation, $19')
    total = total + 19

elif service2 == 'Car wash':
    print('Service 2: Car wash, $7')
    total = total + 7

elif service2 == 'Car wax':
    print('Service 2: Car wax, $12')
    total = total + 12

elif service2 == '-':
    print('Service 2: No service')
    total = total + 0

else:
    print('Service 2: Invalid option')

print()
print('Total: ${}'.format(total))
