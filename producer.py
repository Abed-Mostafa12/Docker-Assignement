from flask import Flask
import random
import time

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def generate_data():
    random_number = random.randint(1, 1000)
    return f"rand: {random_number}\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
