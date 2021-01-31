# chapter06-4-1
# Asyncio
# 비동기 I/O Coroutine 작업
# Generator -> 반복적인 객체 Return(yield)
# 즉, 실행 Stop -> 다른 작업으로 위임 -> Stop 지점 부터 재실행 원리
# Non-Blocking 비동기 처리에 적합

# BlockIO
# 순차 실행

import timeit
from urllib.request import urlopen

urls = ['https://daum.net', 'https://google.com', 'https://apple.com', 'https://tistory.com','https://github.com','https://gmarket.co.kr']

start = timeit.default_timer()

# 순차 실행부
for url in urls:
    print('Start', url)
    # 실제요청
    text = urlopen(url)
    # print('Contents', dir(text))
    # 실제내용
    # print('Contents', text.read())
    print('Done', url)


# 완료시간 - 시작시간
duration = timeit.default_timer() - start

# 총 실행 시간
print('Total Time', duration)