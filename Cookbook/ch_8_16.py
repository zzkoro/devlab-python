import time

class Date:
    # 기본 생성자
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    #  대안 생성자
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)