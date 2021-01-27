import json
with open("dictionary.json", "r") as read_file:
    data = json.load(read_file)
    alphabet = data['alphabet']
    morse = data['morse']
    keymash = data['keymash']
    keymashExtra = data['keymashExtra']
    
def decode(encodedText):
    # Replace every occurrence s with . and k with -
    decodedText = encodedText.replace('s', '.').replace('k', '-');

    # If character is alphanumeric, i.e not a dit or dah, return '0'
    # .split('0') to delimit the resulting list by 0s, preserving spaces
    decodedText = "".join(['0' if x.isalnum() else x for x in decodedText]).split('0');

    # using morse[] as reference to find the corresponding index on alphabet[]
    decodedText = "".join([alphabet[morse.index(x)] for x in decodedText]);

    return decodedText
