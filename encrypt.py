from flask import jsonify

from keysplit import keySplit

def encrypt(user_key, message):
    key1, key2, key3 = keySplit(user_key)
    b = [ord(c) for c in message] #splits the message into an array of characters
    count = len(message)
    y = 0
    Xn = [0] * count #creates an array of 0's eqaul to the length of the message
    while count > 0: #encrypts the message a character at a time and fills the Xn array
        if b[y] > key3:
            Xn[y] = b[y] + key1
            if Xn[y] > 126:
                d = Xn[y] - 126
                Xn[y] = ((key3 + 1) + key1) - d
        elif b[y] <= key3:
            Xn[y] = b[y] - key2
            if Xn[y] < 32:
                d = 32 - Xn[y]
                Xn[y] = (key3 - key2) + d
        count = count - 1
        y = y + 1

    eMessage = [''.join(chr(i) for i in Xn)] #combines all the characters back into a single string
    res = str(eMessage)[2:-2] #trims off the [''] from the response
    return jsonify(message=res)

"""@app.route('/_get_current_user')
def get_current_user():
    return jsonify(
        username=g.user.username,
        email=g.user.email,
        id=g.user.id
    )
"""