# N = int(input())
# hh, mm, ss = 0, 0, 0

# cnt = 0 
# while True:
#     ss += 1
#     if ss == 60:
#         ss = 0
#         mm += 1
#         if mm == 60:
#             mm = 0
#             hh += 1
#             if hh == N+1:
#                 break
#     clk = str(hh) + str(mm) + str(ss)
#     if "3" in clk:
#         cnt += 1

# print("최종 결과 : {}".format(cnt))

################### 2023-09-25 ###################
n = int(input())

# h시 m2m1분 s2s1초 
h, m2, m1, s2, s1 = 0, 0, 0, 0, 0
result = 0
while h < 6:
    s1 += 1
    if s1 == 10:
        s1 = 0
        s2 += 1
        if s2 == 6:
            s2 = 0
            m1 += 1
            if m1 == 10:
                m1 = 0
                m2 += 1
                if m2 == 6:
                    m2 = 0
                    h += 1
                    
    if h == 3 or m2 == 3 or m1 == 3 or s2 == 3 or s1 == 3:
        result += 1
        
print("결과값 : {}".format(result))