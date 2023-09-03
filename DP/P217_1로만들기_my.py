import time
x = int(input())

start_time = time.time()

cnt = 0
def solution(x):
    global cnt
    
    if x == 1:
        return cnt
    
    cnt += 1
    if x % 5 == 0:
        x = x // 5
        return solution(x)
        
    elif x % 3 == 0:
        x = x // 3
        return solution(x)
        
    elif x % 2 == 0:
        x = x // 2
        return solution(x)
        
    else:
        x = x - 1
        return solution(x)

print(solution(x))

end_time = time.time()
print("수행시간 :{}".format(end_time-start_time))
