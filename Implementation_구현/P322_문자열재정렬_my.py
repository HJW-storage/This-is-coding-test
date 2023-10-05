s = list(input())

# ord('A') - 65  ord('Z') - 90
# ord('a') - 97  ord('z') - 122
# ord('0') - 48  ord('1') - 49  ord('9') - 57

# print(ord('97'))
# K1KA5CB7
# print(type(ord(s[0])))
# print(s.sort())

def change_alphabet(x):
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L',
                'M','N','O','P', 'Q','R','S','T', 'U', 'V','W','X','Y','Z']

    return alphabet[x-65]
    
alphabet_list = []
num_sum = 0
for i in s:
    if ord(i) >= 48 and ord(i) <= 57:
        num_sum += (ord(i) - 48)
    else:
        alphabet_list.append(ord(i))
        
alphabet_list.sort()
for i in range(len(alphabet_list)):
    # alphabet_list[i] = change_alphabet(alphabet_list[i])
    print(change_alphabet(alphabet_list[i]), end= '')
print(num_sum)