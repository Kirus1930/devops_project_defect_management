from flask import Flask
import requests
import random

app = Flask(__name__)

@app.route('/')
def home():
    number = random.randint(1, 100)
    response = requests.get(f'http://service2:5001/process?number={number}')
    return f"Service1 generated: {number}. Service2 responded: {response.text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)