from flask import Flask, jsonify
from random_num_gen import random_number_generator
from genunoqnumbers import mysql_connection, mysql_get_listof_already_generated_numbers, mysql_insert_random_generated_numbers, myresult

app = Flask(__name__)
@app.route('/random', methods=['GET'])
def get_data():
    random_number = random_number_generator()
    db_insert = mysql_insert_random_generated_numbers(random_number)
    data = {'random':random_number}

    return jsonify(data), db_insert

if __name__ == '__main__':
        app.run(debug=True)
