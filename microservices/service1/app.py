from flask import Flask, jsonify
import requests
import random
import os

app = Flask(__name__)

@app.route('/')
def home():
    hostname = os.uname().nodename
    number = random.randint(1, 100)
    
    # Отправляем запрос к service2 через внутреннюю сеть Docker
    response = requests.get(f'http://service2:5001/process?number={number}')
    
    return jsonify({
        "service": "Service1",
        "hostname": hostname,
        "generated_number": number,
        "service2_response": response.json() if response.status_code == 200 else "Error"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)