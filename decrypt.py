__author__ = 'ecnavda'

EncryptedKey = '910187075487580862510254'

AdobeCipher = []
AdobeCipher.append('0000000001')
AdobeCipher.append('5038647192')
AdobeCipher.append('1456053789')
AdobeCipher.append('2604371895')
AdobeCipher.append('4753896210')
AdobeCipher.append('8145962073')
AdobeCipher.append('0319728564')
AdobeCipher.append('7901235846')
AdobeCipher.append('7901235846')
AdobeCipher.append('0319728564')
AdobeCipher.append('8145962073')
AdobeCipher.append('4753896210')
AdobeCipher.append('2604371895')
AdobeCipher.append('1426053789')
AdobeCipher.append('5038647192')
AdobeCipher.append('3267408951')
AdobeCipher.append('5038647192')
AdobeCipher.append('2604371895')
AdobeCipher.append('8145962073')
AdobeCipher.append('7901235846')
AdobeCipher.append('3267408951')
AdobeCipher.append('1426053789')
AdobeCipher.append('4753896210')
AdobeCipher.append('0319728564')

DecryptedKey = ''

counter = 0

for x in AdobeCipher:
    if counter % 4 == 0 and counter > 0 :
        DecryptedKey += '-'
    DecryptedKey += x[int(EncryptedKey[counter])]
    counter += 1

print DecryptedKey