def fibonacci_recursive(n, counter):
    # 함수가 호출될 때마다 카운트 증가
    counter['count'] += 1
    
    # 기본 조건 (Base Case)
    if n <= 1:
        return n
    
    # 재귀 호출
    return fibonacci_recursive(n - 1, counter) + fibonacci_recursive(n - 2, counter)

# 테스트 실행
n_list = [1, 2, 3, 4]

print(f"{'n값':>5} | {'결과값':>10} | {'총 호출 횟수 (연산량)':>20}")
print("-" * 45)

for n in n_list:
    call_info = {'count': 0}
    result = fibonacci_recursive(n, call_info)
    print(f"{n:>5} | {result:>10} | {call_info['count']:>20,}")

import time

def fibonacci_recursive(n):
    # 기본 조건 (Base Case)
    if n <= 1:
        return n
    # 재귀 호출
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# 테스트할 n의 범위
n_values = [1, 2, 3, 4]

print(f"{'n값':>5} | {'결과값':>12} | {'수행 시간 (초)':>15}")
print("-" * 40)

for n in n_values:
    start_time = time.time()  # 시작 시간 저장
    result = fibonacci_recursive(n)
    end_time = time.time()    # 종료 시간 저장
    
    elapsed_time = end_time - start_time
    print(f"{n:>5} | {result:>12} | {elapsed_time:>15.10f}s")
