#BRYANCHAVARRIA
#1657040

num_lemon_cups = float(input('Enter amount of lemon juice (in cups):\n'))
num_water_cups = float(input('Enter amount of water (in cups):\n'))
num_nectar_cups = float(input('Enter amount of agave nectar (in cups):\n'))
num_servings_cups = float(input('How many servings does this make?\n'))

print('\nLemonade ingredients - yields {:.2f} servings'.format(num_servings_cups))
print('{:.2f} cup(s) lemon juice'.format(num_lemon_cups))
print('{:.2f} cup(s) water'.format(num_water_cups))
print('{:.2f} cup(s) agave nectar'.format(num_nectar_cups))

num_servings_required = float(input('\nHow many servings would you like to make?\n'))

print('\nLemonade ingredients - yields {:.2f} servings'.format(num_servings_required))
print('{:.2f} cup(s) lemon juice'.format(num_lemon_cups * num_servings_required / num_servings_cups))
print('{:.2f} cup(s) water'.format(num_water_cups * num_servings_required / num_servings_cups))
print('{:.2f} cup(s) agave nectar'.format(num_nectar_cups * num_servings_required / num_servings_cups))

print('\nLemonade ingredients - yields {:.2f} servings'.format(num_servings_required))
print('{:.2f} gallon(s) lemon juice'.format(num_lemon_cups * num_servings_required / num_servings_cups / 16))
print('{:.2f} gallon(s) water'.format(num_water_cups * num_servings_required / num_servings_cups / 16))
print('{:.2f} gallon(s) agave nectar'.format(num_nectar_cups * num_servings_required / num_servings_cups / 16))