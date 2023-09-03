import random
from elements import chemical_elements
def quiz(no_of_rounds,upto_atomic_number):
    print(f'\n\nThis Round will be of {no_of_rounds} questions.\n\n')
    win = 0

    for i in range(1,no_of_rounds):
        teplememt = chemical_elements[random.randrange(0,upto_atomic_number)]
        try:
            i = int(input(f'What is the atomic no. of {teplememt["name"]} : '))
        except ValueError:
            i = -1
        if i == teplememt["atomic_number"]:
            win += 1
            print(f'\ncorrect!!\n\nCurrent Score : {win}\n')
        elif i != -1:
            print(f'\nincorrect!!\n\nCurrent Score : {win}\n')
        else:
            print('\nEnter a number!!. \n')
    print(f"Your score = {win}/{no_of_rounds}.")
    input()
