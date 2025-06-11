from flask import Flask, jsonify
import random

random_nums = []

def random_number_generator():
    num = random.randrange(0,1000000)
    random_nums.append(num)
    print(random_nums)
    return num



