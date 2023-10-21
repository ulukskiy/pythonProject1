import random
import emoji
from termcolor import colored

def play_casino(selected_slot):
    winning_slot = random.randint(1, 30)

    if selected_slot == winning_slot:
        print(colored('ты выиграл!!!  :red_heart:','green'))
    else:
        print(colored('Ты проиграл!!! ','red'))

