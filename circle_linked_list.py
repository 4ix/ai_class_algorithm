# %%
# 이중 링크드 리스트 작성
# 처음 node 생성 시 -> HEAD에 node 저장 
# 마지막에 node 삽입시 -> 마지막 노드 next에 node 저장, node.prev에 마지막 node 저장
#                           TAIL <- node
# 중간 node 삽입시 -> node의 next <- curr node, curr prev next <- node
#                     node의 prev <- curr prev node, curr prev <- node
#                       이전 노드의 next에 node 저장,
#                           이전 노드의 next에 node 저장,
# 처음 node 삽입시 -> HEAD의 prev <- node, node의 next <- HEAD, HEAD <- node

# %%
class Node:
    # seq = 0
    def __init__(self):
        self.pre = None
        self.data = {'name': None, 'score': None}
        self.next = None

HEAD = TAIL = None
CNT = 0

# %%
def menu_prt():
    print(' 1. 자료입력 -> ')
    print(' 2. 자료삭제 ')
    print(' 3. 자료 조회  ')  
    print(' 9. 프로그램 종료 ')  
    print('==================================')    
    print('선택 > ',end='')
    menu = input()
    return menu

def add_node():
    global HEAD, CNT
    # 생성
    node = Node() # 빈 노드 생성
    # node.data = input('자료 입력: ' ) # node.data 에 자료 입력
    node.data['name'] = input('이름 입력: ' ) # node.data 에 자료 입력
    node.data['score'] = input('점수 입력: ' ) # node.data 에 자료 입력
    CNT += 1
    # # 시퀀스 추가
    # Node.seq += 1
    # node.no = Node.seq
    # # 시퀀스 추가 종료

    # 처음 node 생성 시 -> head에 node 저장
    if HEAD == None:
        HEAD = TAIL = node # HEAd, TAIL에 node 저장
        print(HEAD.pre)
        print(HEAD.data)
        print(HEAD.next)
        return

    elif HEAD.data['score'] > node.data['score']: # 1) HEAD 앞에 삽입하는 경우 (맨 앞에 삽입)
        HEAD.pre = node
        node.next = HEAD
        HEAD = node
        return
    
    curr = HEAD
    while curr.next != HEAD: #2) 중간에 삽입하는 경우 / 현재 node(curr)의 next값이 HEAD가 아니면 수행 
        if curr.data['score'] > node.data['score']: # 현재 node(curr)의 data 값이 node의 data값 보다 클 때
            node.next = curr # 삽입 node.next에 현재 node(curr) 저장
            curr.prev = node # 이전 prev.next에 node 저장
            node.prev = curr.prev
            return
        prev = curr # 현재 node를 prev로 저장
        curr = curr.next # 다음 node로 이동

        
    # 3) 마지막에 노드 삽입 경우( 마지막 node.next에 node 저장 / node.next 에 head 저장)
    if curr.data['score'] > node.data['score']: # 현재 node(curr)의 data 값이 node의 data값 보다 클 때
        # 중간 삽입
        node.next = curr # 삽입 node.next에 현재 node(curr) 저장
        prev.next = node # 이전 prev.next에 node 저장
        return
    else:
        last.next = node
        node.prev = last
        TAIL = node

def del_node():
    global HEAD, CNT
    name = input('삭제할 자료 입력 -> ')
    # 처음 node 삭제 -> HEAD = HEAD.next
    # 마지막 node.next 에 HEAD.next 
    if HEAD.data['name'] == name:
        CNT -= 1
        last = HEAD
        while last.next != HEAD:  # 마지막 node 검색
            last = last.next    
        if last == HEAD: # 노드가 1개 있을 때 삭제할 경우
            HEAD = None
            CNT = 0
            del last
        else:
            del last.next  # 메모리 삭제
            HEAD = last.next = HEAD.next           
        return
    
    curr = HEAD
    while curr.next != HEAD:
        # 중간 node 삭제 -> prev.next = curr.next
        if curr.data['name'] == name:
            CNT -= 1
            prev.next = curr.next
            del curr     # curr node 메모리 삭제
            return
        
        prev = curr
        curr = curr.next
        
    # 마지막 node 삭제  -> prev.next = curr.next
    if curr.data['name'] == name:
        CNT -= 1
        prev.next = curr.next
        del curr    # curr node 메모리 삭제
        return

def list_node(reverse = False):
    global HEAD, TAIL
    if HEAD == None:
        return
        
    if reverse:
        curr = TAIL
    else:
        curr = HEAD

    while curr:
        print(f"{curr.data['name']} : {curr.data['score']}")
        if reverse:
            curr = curr.prev
        else:
            curr = curr.next

# %%
while True:
    menu = menu_prt()
    if menu == '1':
        add_node()
    elif menu == '2':   
        del_node()
    elif menu == '3':
        list_node()
    elif menu == '9':
        break


