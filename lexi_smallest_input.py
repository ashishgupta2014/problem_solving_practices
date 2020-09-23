def lexi(s, chars, n):
    j = 0
    for i in s:
        if i == '>':
            chars[j+1], chars[j] = chars[j], chars[j+1]
        j += 1
    print(''.join(chars))
s = '<<<>'
chars = []
for i in range(97, len(s)+98):
    chars.append(chr(i))
print(chars)
lexi(s, chars, len(chars))
