import random

random_nums = []

def random_number_generator():
    while True:
        random_number = random.randrange(0,20)
        if random_number not in random_nums:
            random_nums.append(random_number)
            return random_number



