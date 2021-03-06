import random;
import json
with open("dictionary.json", "r") as read_file:
    data = json.load(read_file)
    alphabet = data['alphabet']
    morse = data['morse']
    keymash = data['keymash']
    keymashExtra = data['keymashExtra']

def encode(inputText):
    # Convert to keymash list
    encodedText = [keymash[alphabet.index(x)] for x in inputText];

    # Convert to string delimited by 0s
    encodedText = '0'.join(encodedText);
    # Replace whitespaces with a random element from keymashExtra
    # then return as a string
    encodedText = ''.join([x.replace('0', random.choice(keymashExtra)) for x in encodedText])
    return encodedText;

