# da01_queue.py
# 큐 자료구조 구현

# 함수 선언
def isQururFull():
    global SIZE, queue, front, rear
    if rear == SIZE - 1:
        return True
    else:
        return False
    
def isQueueEmpty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if isQururFull():
        print('Queue is full')
    else:
        rear += 1
        queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is empty')
        return None
    else:
        front += 1
        data = queue[front]
        queue[front] = None
        return data
    
def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is empty')
        return None
    else:
        return queue[front+1]

# 초기화
SIZE = int(input('큐크기 입력 > '))
queue = [None for _ in range(SIZE)]
front = rear = -1

## 메인 모듈
if __name__ == '__main__':
    print('메인시작')
    while True:
        select = input('삽입(I)/추출(E)/확인(V)/종료(Q)').upper

        if select == 'Q':
            break
        elif select == 'I':
            data = input('데이터 입력 > ')
            enQueue(data)
            print(f'큐 상태 : {queue}')
        else:
            print('입력 오류')