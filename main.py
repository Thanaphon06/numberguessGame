import random
from re import X


num = random.randint(0, X)

attempt = 4 
msg = 'You Lost!'   

while attempt > 0:
    user_input = int(input('Enter Number: '))
    if user_input > num:
        print("Sorry, guess again. Too hight")
    elif user_input < num:
        print("Sory,guess again. Too low")
    else:
        print("yay u woon bab")
        break