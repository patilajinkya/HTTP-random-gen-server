from flask import Flask, jsonify
from random_num_gen import random_number_generator
from save_generated_numbers import mysql_insert_random_generated_numbers, mysql_get_listof_already_generated_numbers

existing_numbers = mysql_get_listof_already_generated_numbers() # Get the list of already generated number if any.
app = Flask(__name__) # Created a flask instance
@app.route('/random', methods=['GET']) # Mapped /random endpoint path to <get_data> function.
def get_data():
    random_number = random_number_generator(existing_numbers)    # Generating a random number by providing list of already generated number to exclude
    print(random_number)
    mysql_insert_random_generated_numbers(random_number)  # Inserting a number to mysql DB to make it persistent.
    data = {'random':random_number}

    return jsonify(data)

if __name__ == '__main__':
        app.run(port=8001, debug=True)
