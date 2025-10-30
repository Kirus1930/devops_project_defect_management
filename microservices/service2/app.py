from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/process')
def process():
    hostname = os.uname().nodename
    number = request.args.get('number', type=int)
    
    if number is None:
        return jsonify({"error": "Number parameter is required"}), 400
    
    result = number ** 2
    
    return jsonify({
        "service": "Service2",
        "hostname": hostname,
        "input_number": number,
        "result": result
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)