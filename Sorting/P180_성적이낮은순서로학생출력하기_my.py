N = int(input())

arr = []
for i in range(N):
    name, score = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 리스트에 추가.
    arr.append([name, int(score)])
    
arr_sco = sorted(arr, key=lambda x: x[1])

for i in range(N):
    print(arr_sco[i][0], end= ' ')