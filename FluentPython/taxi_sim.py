import random
import collections
import queue
import argparse
import time

DEFAULT_NUMBER_OF_TAXIES = 3
DEFAULT_END_TIME = 180
SEARCH_DURATION = 5
TRIP_DURATION = 20
DEPARTURE_INTERVAL = 5

Event = collections.namedtuple('Event', 'time proc action')

# TAXI_PROCESS 시작
def taxi_process(ident, trips, start_time=0):
    """ 각 상태 변화마다 이벤트를 발생시키는 시뮬레이터에 양보한다. """
    time = yield Event(start_time, ident, 'leave garage')
    for i in range(trips):
        time = yield Event(time, ident, 'pick up passenger')
        time = yield Event(time, ident, 'drop off passenger')

    yield Event(time, ident, 'going home')
# TAXI_PROCESS 끝

# TAXI_SIMULATOR 시작
class Simulator:
    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)

    def run(self, end_time):
        """ 시간이 만료될 때까지 이벤트를 스케줄링하고 출력한다. """
        # 각 택시마다 첫번째 이벤트를 스케줄링한다.
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)
        # 시뮬레이션 메인 루프
        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print('*** end of events ***')
                break
            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event  
            print('taxi:', proc_id, proc_id * '   ', current_event)
            active_proc = self.procs[proc_id]
            next_time = sim_time + compute_duration(previous_action)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.events.put(next_event)
        else:
            msg = '*** end of simulation time: {} events pending ***'
            print(msg.format(self.events.qsize()))
# TAXI_SIMULATOR 끝

def compute_duration(previous_action):
    """ 지수 분포를 이용해서 행동 기간을 계산한다. """
    if previous_action in ['leave garage', 'drop off passenger']:
        # 손님 없이 배회하는 상태가 됨
        interval = SEARCH_DURATION
    elif previous_action == 'pick up passenger':
        # 손님을 태우고 운행하는 상태가 됨
        interval = TRIP_DURATION
    elif previous_action == 'going home':
        interval = 1
    else:
        raise ValueError('Unknown previous_action: %s' % previous_action)
    return int(random.expovariate(1 / interval)) + 1

def main(end_time=DEFAULT_END_TIME, num_taxies=DEFAULT_NUMBER_OF_TAXIES, seed=None):
    """ 난수 생성기 초기화, 프로세스 생성, 시뮬레이션 실행 """
    if seed is not None:
        random.seed(seed)   # 다시 생성할 수 있는 결과를 가져온다.

    taxies = {i: taxi_process(i, (i+1)*2, i*DEPARTURE_INTERVAL)
                for i in range(num_taxies)}
    sim = Simulator(taxies)
    sim.run(end_time)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Taxi fleet simulator.')
    parser.add_argument('-e', '--end-time', type=int, default=DEFAULT_END_TIME, help='simulation end time; default = %s' % DEFAULT_END_TIME)
    parser.add_argument('-t', '--taxies', type=int, default=DEFAULT_NUMBER_OF_TAXIES, help='number of taxies running; default = %s' % DEFAULT_NUMBER_OF_TAXIES)
    parser.add_argument('-s', '--seed', type=int, default=None, help='random generator seed (for testing)')

    args = parser.parse_args()
    main(args.end_time, args.taxies, args.seed)