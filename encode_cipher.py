def encode_vigenere_cipher(message, keyword):
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    final_messsage = ""
    key = ""
    length = 0
    for letter in message:
        if letter in alphabet:
            key += keyword[length % len(keyword)]
            length += 1
        else:
            key += letter
    
    for i in range(len(message)):
        if message[i] in alphabet:
            final_messsage += alphabet[(alphabet.index(message[i]) - alphabet.index(key[i])) % 26]
        else:
            final_messsage += message[i]
    
    return final_messsage