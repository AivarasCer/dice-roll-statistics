import random
import time


def get_number_of_dice():
    while True:
        try:
            number_of_dice = int(input('Enter how many dice you want to roll:\n> '))
            if number_of_dice > 0:
                return number_of_dice
            else:
                print('Please enter a positive integer.')
        except ValueError:
            print('Invalid input. Please enter a valid integer.')


def simulate_rolls(number_of_dice, simulations=1000000):
    results = {i: 0 for i in range(number_of_dice, (number_of_dice * 6) + 1)}
    print(f'Simulating {simulations:,} rolls of {number_of_dice} dice...')
    last_print_time = time.time()

    for i in range(simulations):
        if time.time() > last_print_time + 1:
            print(f'{round(i / simulations * 100, 1)}% done...')
            last_print_time = time.time()

        total = sum(random.randint(1, 6) for _ in range(number_of_dice))
        results[total] += 1

    return results


def display_results(results, number_of_dice, simulations):
    print('TOTAL - ROLLS - PERCENTAGE')
    for total, rolls in sorted(results.items()):
        percentage = round(rolls / simulations * 100, 1)
        print(f'{total:>5} - {rolls:>6} rolls - {percentage:>6.1f}%')


def main():
    number_of_dice = get_number_of_dice()
    num_simulations = 1000000
    results = simulate_rolls(number_of_dice, num_simulations)
    display_results(results, number_of_dice, num_simulations)


if __name__ == "__main__":
    main()
