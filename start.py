from decouple import config
from logic import play_casino, colored

def main():
    initial_money = float(config('MY_MONEY', default='1000000'))
    money = initial_money

    while money > 0:
        print(f'Ваш текущий капитал: ${money}')
        bet = float(input('Сделайте ставку: $'))

        if bet > money:
            print('Вы не можете поставить больше, чем у вас есть!')
            continue

        selected_slot = int(input('Выберите слот (от 1 до 30): '))

        if play_casino(selected_slot):
            money += bet
            print(f'Вы выиграли ${bet}!')
        else:
            money -= bet
            cc=colored(f'Вы проиграли ${bet}',"red")
            print(cc)

        play_again = input('Хотите сыграть еще (да/нет)? ').strip().lower()
        if play_again != 'да':
            break

    if money > initial_money:
        print(f'Поздравляем, вы в выигрыше! Ваш конечный капитал: ${money}')
    else:
        print(f'Вы проиграли. Ваш конечный капитал: ${money}')

if __name__ == '__main__':
    main()
