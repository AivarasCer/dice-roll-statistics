import random
from tqdm import tqdm


def get_dice_configuration():
    while True:
        try:
            number_of_dice = int(input('Enter how many dice you want to roll:\n> '))
            if number_of_dice <= 0:
                print('Please enter a positive integer.')
                continue

            sides_of_dice = int(input('Enter the number of sides on each die:\n> '))
            if sides_of_dice <= 0:
                print('Please enter a positive integer.')
                continue

            return number_of_dice, sides_of_dice
        except ValueError:
            print('Invalid input. Please enter a valid integer.')


def simulate_rolls(number_of_dice, sides_of_dice, simulations=1000000):
    results = {i: 0 for i in range(number_of_dice, number_of_dice * sides_of_dice + 1)}
    print(f'Simulating {simulations:,} rolls of {number_of_dice} dice with {sides_of_dice} sides each...')

    for _ in tqdm(range(simulations), desc="Rolling Dice"):
        total = sum(random.randint(1, sides_of_dice) for _ in range(number_of_dice))
        results[total] += 1

    return results


def display_results(results, simulations):
    print('TOTAL - ROLLS - PERCENTAGE')
    for total, rolls in sorted(results.items()):
        percentage = round(rolls / simulations * 100, 1)
        print(f'{total:>5} - {rolls:>6} rolls - {percentage:>6.1f}%')


def main():
    number_of_dice, sides_of_dice = get_dice_configuration()
    num_simulations = 1000000
    results = simulate_rolls(number_of_dice, sides_of_dice, num_simulations)
    display_results(results, num_simulations)


if __name__ == "__main__":
    main()
