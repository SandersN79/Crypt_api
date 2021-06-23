from flask import Flask, request
from encrypt import encrypt
from decrypt import decrypt

app = Flask(__name__)

@app.route('/encrypt/', methods=['POST'])
def encryptMessage():
    #content = request.get_json('userkey') this will return all the data
    user_key = request.json.get('user_key')
    message = request.json.get('message')
    # '\ dont work in message string. Prob away to work around it. \ is an escape character.
    # gonna have to parse " and ' in the string as \" or \' for it to show in the string
    return encrypt(user_key, message)

@app.route('/decrypt/', methods=['POST'])
def decryptMessage():
    user_key = request.json.get('user_key')
    message = request.json.get('message')
    return decrypt(user_key, message)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9999)
