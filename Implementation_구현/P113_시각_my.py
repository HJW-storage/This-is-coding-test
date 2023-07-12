N = int(input())
hh, mm, ss = 0, 0, 0

cnt = 0 
while True:
    ss += 1
    if ss == 60:
        ss = 0
        mm += 1
        if mm == 60:
            mm = 0
            hh += 1
            if hh == N+1:
                break
    clk = str(hh) + str(mm) + str(ss)
    if "3" in clk:
        cnt += 1

print("최종 결과 : {}".format(cnt))
