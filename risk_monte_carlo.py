import random

DEBUG = False
number_of_simulations = 3
attack_start_armies = 7
defense_start_armies = 3
results = []


def simulate_round(attack, defense):
    attack_dice = min(attack-1, 3)
    defense_dice = defense
    attack_roll = [random.randint(1, 6) for _ in range(attack_dice)]
    defense_roll = [random.randint(1, 6) for _ in range(defense_dice)]
    attack_roll.sort(reverse=True)
    defense_roll.sort(reverse=True)
    attack_loss = 0
    defense_loss = 0
    for _ in range(min(attack_dice, defense_dice)):
        offensive_roll = attack_roll.pop()
        defensive_roll = defense_roll.pop()
        if defensive_roll >= offensive_roll:
            attack_loss += 1
        else:
            defense_loss += 1
    return attack-attack_loss, defense-defense_loss



for i in range(number_of_simulations):
    attack_armies = attack_start_armies
    defense_armies = defense_start_armies
    if DEBUG:
        print("Simulation {} start:".format(i+1))
    while attack_armies > 1:
        attack_armies, defense_armies = simulate_round(attack_armies, defense_armies)
        if defense_armies == 0:
            results.append(attack_armies)
            break
        if attack_armies == 1:
            results.append(-1)
            break
        if DEBUG:
            print("\tattackers: {}\tdefenders: {}".format(attack_armies, defense_armies))
print(results)
