from itertools import product
from itertools import combinations_with_replacement

data = ['a', 2, 3]
result = list(product(data, repeat=2)) # 중복 순열
print(result)
result = list(combinations_with_replacement(data, 2)) # 중복 조합
print(result)