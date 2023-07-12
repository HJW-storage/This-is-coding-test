# 함수 기본 - global
a = 0

def func():
    global a
    a += 1

for _ in range(10):
    func()

print(a)