from flask import Flask, jsonify
from random_num_gen import random_number_generator
from genunoqnumbers import mysql_insert_random_generated_numbers, process_myresults_to_maintain_list, mysql_get_listof_already_generated_numbers

app = Flask(__name__)
@app.route('/random', methods=['GET'])
def get_data():
    existing_numbers = mysql_get_listof_already_generated_numbers()
    processed_numbers = process_myresults_to_maintain_list(existing_numbers)
    random_number = random_number_generator(processed_numbers)
    db_insert = mysql_insert_random_generated_numbers(random_number)
    data = {'random':random_number}

    return jsonify(data), db_insert

if __name__ == '__main__':
        app.run(debug=True)
