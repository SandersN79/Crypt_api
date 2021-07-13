from flask import Flask, request
from encrypt import encrypt
from decrypt import decrypt

app = Flask(__name__)

@app.route('/encrypt/', methods=['POST'])
def encryptMessage():
    #content = request.get_json('userkey') this will return all the data
    user_key = request.json.get('user_key')
    message = request.json.get('message')
    #print(request.json.get('message'))
    return encrypt(user_key, message)

@app.route('/decrypt/', methods=['POST'])
def decryptMessage():
    user_key = request.json.get('user_key')
    message = request.json.get('message')
    #print(request.json.get('message'))
    return decrypt(user_key, message)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9999)
