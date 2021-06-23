from flask import jsonify

from keysplit import keySplit

#See encrypt.py for notes
def decrypt(user_key, message):
    key1, key2, key3 = keySplit(user_key)
    b = [ord(c) for c in message]
    count = len(message)
    y = 0
    Xn = [0] * count
    while count > 0:
        if b[y] > key3 and b[y] <= (key3 + key1):
            d = b[y] - (key3+1)
            Xn[y] = 126 - d
        elif b[y] > (key3 + key1):
            Xn[y] = b[y] - key1
        elif b[y] <= key3 and b[y] >= (key3-key2):
            d = (key3+key2) - b[y]
            Xn[y] = (32-key2) + d
        elif b[y] < (key3-key2):
            Xn[y] = b[y] + key2
        count = count - 1
        y = y + 1
    dMessage = [''.join(chr(i) for i in Xn)]
    res = str(dMessage)[2:-2]
    return jsonify(message=res)