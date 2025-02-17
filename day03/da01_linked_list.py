# da01_linked_list.py
# 단순 열결리스트

## 전역변수
memory = [] # 컴퓨터 메모리처럼 보이게 만든 변수
head, prev, curr = None, None, None # 항상 첫번째 노드, curr바로 앞의 노드, 현재 선택한 노드
dataArray = ['다현', '정연', '쯔위', '사나', '지효']    # 연결리스트를 만들 데이터

class Node:
    def __init__(self, data):
        self.__data = data
        self.__link = None

    def setLink(self, link):
        self.__link = link
    
    def getData(self):
        return self.__data

    def getLink(self):
        return self.__link

def printNodes(start):
    curr = start
    if curr == None: return

    print(curr.getData(), end='->')

    while curr.getLink() != None:    # 현재링크의 다음링크가 있는동안 
        curr = curr.getLink()    # 다음 노드를 가리킴
        if curr.getLink() == None:  # 더이상 다음 노드가 없으니 화살표 필요없음
            print(curr.getData(), end=' ')
        else:
            print(curr.getData(), end='->')

    print() # 그냥 한줄 내려줌


# 연결리스트 생성 구현
if __name__ == '__main__':  # 시작모듈일때

    node = Node(dataArray[0])  # '다현' 사용
    head = node
    memory.append(node)

    for name in dataArray[1:]:  # '정연'부터 사용
        prev = node # 다현이 들어있는 노드를 prev 할당
        node = Node(name)   # 0/정연, 1/쯔위, 2/사나, /지효
        prev.setLink(node)    # 이전노드에 현재노드를 연결
        memory.append(node)

    printNodes(head)
    # 5개 데이터를 가지는 연결리스트
