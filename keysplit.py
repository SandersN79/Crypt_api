def keySplit(user_key): #takes the user key and splits it into 3 integers based on spaces in the user_key
    keySplit = user_key.split(' ')
    key1 = int(keySplit[0])
    key2 = int(keySplit[1])
    key3 = int(keySplit[2])
    return key1, key2, key3
