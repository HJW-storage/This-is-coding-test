n_list = list((input()))

# n_list = list(n)
# print(n_list)
n_len = len(n_list)

left_sum, right_sum = 0, 0
for i in range(n_len//2):
    left_sum += int(n_list[i])
    right_sum += int(n_list[n_len-i-1])
    
if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")