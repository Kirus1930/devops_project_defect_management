from flask import Flask, request

app = Flask(__name__)

@app.route('/process')
def process():
    number = request.args.get('number', type=int)
    result = number ** 2
    return f"Square of {number} is {result}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)