import time

# 처리전 시간 취득
t1 = time.time()

# 처리(샘플로 반복문 작성)
for i in range(1000000):
    i ** 10

# 처리후 시간 취득
t2 = time.time()

# 처리시간 계산
elapsed_time = t2-t1

# 경과 시간 출력
print("처리시간",elapsed_time)