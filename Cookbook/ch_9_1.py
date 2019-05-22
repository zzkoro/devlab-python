# encoding: utf-8
"""
CHAPTER 9. 메타프로그래밍
9.1 함수 감싸기
 - 함수에 추가적인 처리(로깅, 타이밍)를 하는 wrapper layer 넣기
"""
import time
from functools import wraps

def timethis(func):
    '''
    실행시간을 보고하는 데코레이터
    :param func:
    :return:
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result

    return wrapper

@timethis
def countdown(n):
    '''
    Counts down
    :param n:
    :return:
    '''
    while n > 0:
        n -= 1


