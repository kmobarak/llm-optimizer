import random

def pick_random_problems(total_problems, number_to_pick):
    return sorted(random.sample(range(1, total_problems + 1), number_to_pick))

total_problems = 215

number_to_pick = 35

random_problems = pick_random_problems(total_problems, number_to_pick)
print(f"Randomly selected problems (sorted): {random_problems}")
