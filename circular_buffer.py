import threading  # 스레드 사용을 위해 threading 모듈 사용
import time

# 링 버퍼 클래스 정의
class CircularBuffer(threading.Thread):
    # 클래스 생성자
    def __init__(self, buf_size):
        super().__init__()
        self.buf_size = buf_size # 버퍼 사이즈 초기화
        self.queue = [None] * buf_size # 버퍼 초기화
        self.size = 0 # 버퍼 내 현재 원소 개수
        self.front = 0 # 버퍼의 가장 앞부분 인덱스
        self.back = 0 # 버퍼의 가장 뒷부분 인덱스
        self.number = 0 # 버퍼에 넣을 숫자

    # data producer
    def produce(self):
        if self.size == self.buf_size:
            event.wait() # 버퍼가 꽉 차있는 경우 대기

        self.queue[self.back] = self.number # 버퍼에 숫자 append
        self.number += 1 # 다음에 넣을 숫자 늘리기
        self.size += 1 # 사이즈 늘리기
        self.back += 1 # back index 늘리기
        if self.back == self.buf_size:
            self.back = 0 # back index가 max index 넘어가는 경우, 0번 인덱스로 지정

        print(f"produced: {self.queue}")

        event.set() # 대기 해제

        threading.Timer(0.1, self.produce).start()

    # data consumer
    def consume(self):
        if self.size == 0:
            event.wait() # 버퍼가 비어있는 경우 대기

        self.queue[self.front] = None # 버퍼에서 숫자 빼기
        self.size -= 1 # 사이즈 줄이기
        self.front += 1 # front index 늘리기
        if self.front == self.buf_size:
            self.front = 0 # front index가 max index 넘어가는 경우, 0번 인덱스로 지정

        print(f"consumed: {self.queue}")

        event.set() # 대기 해제

        threading.Timer(0.3, self.consume).start()

if __name__ == "__main__":
    event = threading.Event()
    cb = CircularBuffer(buf_size=16)
    cb.produce()
    cb.consume()