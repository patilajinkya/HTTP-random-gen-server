from flask import Flask, jsonify
from random_num_gen import random_number_generator

app = Flask(__name__)
@app.route('/random', methods=['GET'])
def get_data():
    num = random_number_generator()
    data = {'random':num}
    return jsonify(data)

if __name__ == '__main__':
        app.run(debug=True)