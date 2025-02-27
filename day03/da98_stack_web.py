import webbrowser
import time

def isStackFull():
    global SIZE, stack, top
    if (top == SIZE -1):
        return True
    else:
        return False
    
def isStackEmpty():
    global SIZE, stack, top
    if (top == -1):
        return True
    else:
        return False
    
def push(data):
    global SIZE, stack, top
    if isStackFull():
        print('Stack is full!!')
    else:
        top += 1
        stack[top] = data

def pop():
    global SIZE, stack, top
    if isStackEmpty():
        return None
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return data

def peek():
    global SIZE, stack, top
    if isStackEmpty():
        return None
    else:
        return stack[top]

SIZE = 100
stack = [None for _ in range(SIZE)]
top = -1

if __name__ == '__main__':
    urls = ['naver.com', 'daum.net', 'nate.com']

    for url in urls:
        push(url)
        webbrowser.open('http://'+ url)
        print(url, end='-->')
        time.sleep(1)

    print('방문종료')
    time.sleep(5)

    while True:
        url = pop()
        if url == None:
            break
        webbrowser.open('http://'+ url)
        print(url, end='-->')
        time.sleep(1)
    print('방문종료')
