# # n, k 입력
# n, k = map(int, input().split())

# cnt = 0
# while True:
#     if n == 1:
#         print("최종 결과 : {}".format(cnt))
#         break
#     if n % k == 0:
#         n = int(n/k)
#     else:
#         n -= 1
#     cnt += 1

######################### 2023-10-25 #########################
n, k = map(int, input().split())

def solution():
    global n
    cnt = 0
    while n > 1:
        if n % k == 0:
            n = int(n/k)
        else:
            n -= 1
        
        cnt += 1
        
    print(cnt)
    
solution()
# print(n)