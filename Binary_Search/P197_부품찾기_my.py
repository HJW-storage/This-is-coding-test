import sys

def solution_search(parts, ask_parts, start, end):
    for target in ask_parts:
        tmp_start, tmp_end = start, end
        yes_flag = False
        
        while tmp_start <= tmp_end:
            mid = (tmp_start + tmp_end) // 2
            
            if parts[mid] == target:
                yes_flag = True
                break
            elif parts[mid] > target:
                tmp_end = mid - 1
            else:
                tmp_start = mid + 1
                
        if yes_flag == True:
            print("yes", end = ' ')
        else:
            print("no", end = ' ')


n = int(input())
# parts = list(map(int, input().split()))
parts = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
# ask_parts = list(map(int, input().split()))
ask_parts = list(map(int, sys.stdin.readline().rstrip().split()))

parts.sort()    # 오름차순 정렬 
print(parts)

solution_search(parts, ask_parts, 0, n-1)
