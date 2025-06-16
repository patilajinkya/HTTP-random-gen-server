import random
def random_number_generator(existing_numbers):
    random_nums = existing_numbers
    while True:
        random_number = random.randrange(0,20)
        if random_number not in random_nums:
            random_nums.append(random_number) # Appending generated number to the list random_nums
            return random_number



