from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hola mundo"
print(">>", __name__)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80)