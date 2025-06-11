from flask import Flask, jsonify
import random

num = random.randrange(0,1000000)

app = Flask(__name__)

@app.route('/random', methods=['GET'])
def get_data():
    data = {'random':num}
    return jsonify(data)

if __name__ == '__main__':
        app.run(debug=True)