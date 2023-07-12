# 입력
# arr = list(map(int, input().split()))
# print(arr)

# 입력의 추가적인 방법 - 수행시간을 줄일 수 있다.
import sys
print("데이터를 입력하세요 : ", end='')
data = sys.stdin.readline().rstrip()
print(data)

