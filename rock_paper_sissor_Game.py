from random import choice

#rock paper sissor options
choices = ['rock', 'paper', 'sissor']

while True:
    computer_choice = choice(list(enumerate(choices)))
    print("Choose rock, paper, or sissor: ")
    user_choice = input("1. rock\n2. paper\n3. sissor: \n>> ")
    try:
        user_choice_index = (int(user_choice) - 1)
    except:
        print("wrong input")
        continue
    if user_choice_index >= len(choices):
        print("wrong input")
    if user_choice_index == computer_choice[0]:
        print(f"Game Draw !! {computer_choice[1] }--{choices[user_choice_index]}")
    elif user_choice_index > computer_choice[0]:
        print(f"You Won! {computer_choice[1] } -- {choices[user_choice_index]}")
    else:
        print(f"You lost! {computer_choice[1] } -- {choices[user_choice_index]}")
    
    print("Do you want to play again (Y/N) ? ")
    again = input(">> ")
    if again.upper().startswith('Y'):
        continue
    else:
        print('Nice playing with you! ')
        break





