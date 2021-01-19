import random;
alphabet = "abcdefghijklmnopqrstuvwxyz ";
morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", " "];
keymash = ["sk", "ksss", "ksks", "kss", "s", "ssks", "kks", "ssss", "ss", "skkk", "ksk", "skss", "kk", "ks", "kkk", "skks", "kksk", "sks", "sss", "k", "ssk", "sssk", "skk", "kssk", "kskk", "kkss", " "];

keymashExtra = ['d', 'f', 'j', 'l', 'h', 'g', 'a'];

inp = input();

# Convert to keymash list
encode = [keymash[alphabet.index(x)] for x in inp];

# Convert to string delimited by 0s
encode = '0'.join(encode);

# Replace whitespaces with a random element from keymashExtra
# then return as a string
encode = ''.join([x.replace('0', random.choice(keymashExtra)) for x in encode])

print(encode);
