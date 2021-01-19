alphabet = "abcdefghijklmnopqrstuvwxyz ";
morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", " "];

inp = input();

# Replace every occurrence s with . and k with -
stripped = inp.replace('s', '.').replace('k', '-');

# If character is alphanumeric, i.e not a dit or dah, return '0'
# .split('0') to delimit the resulting list by 0s, preserving spaces
stripped = "".join(['0' if x.isalnum() else x for x in stripped]).split('0');

# using morse[] as reference to find the corresponding index on alphabet[]
out = "".join([alphabet[morse.index(x)] for x in stripped]);

print(out);
