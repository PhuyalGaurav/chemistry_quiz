import random
from elements import chemical_elements

def quiz(no_of_rounds,upto_atomic_number):
    print(f'\n\nThis Round will be of {no_of_rounds} questions.\n\n')
    win = 0

    for i in range(1,no_of_rounds):
        teplememt = chemical_elements[random.randrange(0,upto_atomic_number)]
        i = int(input(f'What is the atomic no. of {teplememt["name"]} : '))
        if i == teplememt["atomic_number"]:
            print('correct!!')
            win += 1
        else:
            print('incorrect')
    print(f"Your score = {win}/{no_of_rounds}.")
    input()