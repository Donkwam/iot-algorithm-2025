# da03_binary_tree.py
# 이진 트리 구현

# 초기화
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

# TreeNode클래스 선언
class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

# 메인 모듈
if __name__ == '__main__':
    node = TreeNode()
    node.data = nameAry[0]
    root= node
    memory.append(node)

    for name in nameAry[1:]:
        node = TreeNode()
        node.data = name

        current = root
        while True:
            if name < current.data: # 현재 name이 노드안 데이터보다 작으면, 왼쪽으로
                if current.left == None:
                    current.left = node
                    break
                else:
                    current = current.left  # 왼쪽으로 더 내려감
            else:   # 오른쪽으로 보냄
                if current.left == None:
                    current.right = node
                else:
                    current = current.right

        memory.append(node)
    print('이진탐색 트리 구성완료!')

    findName = input('찾을 이름 입력 > ')
    count = 0
    current = root  # 루트노드부터 검색 시작
    while True:
        if findName == current.data:
            print(f'{findName} 찾음!')
            count += 1
            break
        elif findName < current.data:
            if current.left == None:
                print(f'{findName} 트리에 없음')
                break
            else:
                current = current.left
                count += 1
        else:
            if current.right == None:
                print(f'{findName} 트리에 없음')
            else:
                current = current.right
                count += 1

    print(f'검색 종료 : 총 검색횟수 {count}')