import random

chr_list_from = [' ', 'Æ', 'Ø', 'Å']
chr_list_to = [' ', 'Æ', 'Ø', 'Å']
for i in range(65, 91):
    chr_list_from.append(chr(i))
    chr_list_to.append(chr(i))

random.shuffle(chr_list_to)

encrypt_dict = {}
decrypt_dict = {}
for i in range(len(chr_list_to)):
    encrypt_dict[chr_list_from[i]] = chr_list_to[i]
    decrypt_dict[chr_list_to[i]] = chr_list_from[i]

# print(encrypt_dict)

msg = "HEJ EMMA"
enc = ""

for ch in msg:
    enc += encrypt_dict[ch]

print(enc)

for ch in enc:
    print(decrypt_dict[ch])

