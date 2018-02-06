import random

import matplotlib.pyplot as plt
import matplotlib.style as style

style.use("ggplot")

DEBUG = False
n = 10
a = 7
d = 3


def roll_dice(number_dice):
    res = [random.randint(1, 6) for _ in range(number_dice)]
    res.sort(reverse=True)
    return res


def simulate_round(attack, defense):
    attack_dice = min(attack-1, 3)
    defense_dice = defense
    attack_roll = roll_dice(attack_dice)
    defense_roll = roll_dice(defense_dice)
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


def run_simulations(number_of_simulations, attack_start_armies, defense_start_armies):
    results = {}
    results[1] = 0  # prefill losses in dict since it should always be shown
    for i in range(number_of_simulations):
        attack_armies = attack_start_armies
        defense_armies = defense_start_armies
        if DEBUG:
            print("Simulation {} starts (initial condition: {} attackers and {} defenders:".format(i+1, attack_armies, defense_armies))
        while attack_armies > 1:
            attack_armies, defense_armies = simulate_round(attack_armies, defense_armies)
            if DEBUG:
                print("\tattackers: {}\tdefenders: {}".format(attack_armies, defense_armies))
            if defense_armies == 0:
                if attack_armies not in results.keys():
                    results[attack_armies] = 1
                else:
                    results[attack_armies] += 1
                break
            if attack_armies == 1:
                results[1] +=1
                break
    return results

def graph_results(results, type="line"):
    keys = sorted(results.keys())
    vals = [x for keys,x in results.items()]
    plt.scatter(keys, vals)
    plt.ylim(0, max(vals)+1)
    plt.show()



if __name__ == "__main__":
    result = run_simulations(n, a, d)
    print(result)
    graph_results(result)
